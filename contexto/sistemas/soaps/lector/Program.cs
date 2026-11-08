// Lee tablas y procedimientos de un respaldo .bak de SQL Server sin restaurarlo.
// Uso: lector <respaldo.bak> <salida> <patrón de tablas> <patrón de procedimientos>
// Usa Mdf/ y Mtf/ de https://github.com/Dankular/BAK-SHELL con bakshell.patch aplicado.
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using BakShell.Mdf;
using BakShell.Mtf;

Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);
var (respaldo, salida, patronTablas, patronProcedimientos) = (args[0], args[1], args[2], args[3]);
using var parser = new MtfParser(respaldo);
var mq = parser.FindMqdaStream() ?? throw new Exception("El respaldo no contiene una base de datos");
using var provider = new MtfPageProvider(respaldo, mq.offset, mq.length);
var db = new MdfDatabase(provider);
Directory.CreateDirectory(salida);
var errores = 0;
// Algunas versiones de SOAPS tienen flotantes infinitos, que JSON sólo admite como texto.
var json = new JsonSerializerOptions { NumberHandling = System.Text.Json.Serialization.JsonNumberHandling.AllowNamedFloatingPointLiterals };

foreach (var obj in db.UserTables().Where(o => Regex.IsMatch(o.Name, patronTablas, RegexOptions.IgnoreCase)))
{
    try
    {
        var tabla = db.BuildTable(obj);
        var filas = 0;
        using var writer = new StreamWriter(Path.Combine(salida, obj.Name + ".jsonl"));
        foreach (var row in tabla.Rows())
        {
            var data = new Dictionary<string, object?>();
            for (int i = 0; i < row.Length; i++)
            {
                var v = row[i];
                data[tabla.Schema.Columns[i].Name] = v == null ? null : v.StringVal != null ? v.StringVal : v.Kind switch
                {
                    SqlTypeKind.Float => v.FloatVal,
                    SqlTypeKind.Bit => v.BoolVal,
                    SqlTypeKind.DateTime => v.DateTimeVal,
                    SqlTypeKind.TinyInt or SqlTypeKind.SmallInt or SqlTypeKind.Int or SqlTypeKind.BigInt => v.IntVal,
                    _ => null,
                };
            }
            writer.WriteLine(JsonSerializer.Serialize(data, json));
            filas++;
        }
        Console.WriteLine($"tabla {obj.Name}: {filas} filas");
    }
    catch (Exception e)
    {
        Console.Error.WriteLine($"error en la tabla {obj.Name}: {e.Message}");
        errores++;
    }
}

// Los procedimientos y funciones están en la tabla de sistema 60 (sys.sysobjvalues).
foreach (var page in provider.ObjectPages(60))
foreach (var rec in page.Records(true))
{
    if (rec.FixedData.Length < 13 || rec.FixedData.Span[0] != 1 || rec.VarColumns == null) continue;
    int id = System.Buffers.Binary.BinaryPrimitives.ReadInt32LittleEndian(rec.FixedData.Span[1..]);
    var obj = db.SchObjs.FirstOrDefault(o => o.Id == id);
    if (obj == null || !Regex.IsMatch(obj.Name, patronProcedimientos, RegexOptions.IgnoreCase)) continue;
    for (ushort vi = 0; vi < rec.VarColumns.Count; vi++)
    {
        var (vcomplex, vdata) = rec.VarColumns.Get(vi);
        try
        {
            byte[]? body = vcomplex && vdata.Length == 16 ? LobPointer.Parse(vdata.Span).Read(provider) : vdata.ToArray();
            if (vcomplex && vdata.Length >= 24 && (vdata.Length - 12) % 12 == 0)
            {
                var chunks = new List<byte[]>();
                for (int pos = 12; pos + 12 <= vdata.Length; pos += 12)
                {
                    var ptr = RecordPointer.Parse(vdata.Span[(pos + 4)..(pos + 12)]);
                    if (ptr == null) continue;
                    var chunk = new LobPointer(0, ptr.Value).Read(provider);
                    if (chunk != null) chunks.Add(chunk);
                }
                body = chunks.SelectMany(x => x).ToArray();
            }
            if (body == null || body.Length <= 100) continue;
            var txt = body.Count(b => b == 0) > body.Length / 5 ? Encoding.Unicode.GetString(body) : Encoding.GetEncoding(1252).GetString(body);
            if (!Regex.IsMatch(txt, "create|alter", RegexOptions.IgnoreCase)) continue;
            File.WriteAllText(Path.Combine(salida, obj.Name + ".sql"), txt);
            Console.WriteLine($"procedimiento {obj.Name}");
        }
        catch (Exception e)
        {
            Console.Error.WriteLine($"error en el procedimiento {obj.Name}: {e.Message}");
            errores++;
        }
    }
}
return errores == 0 ? 0 : 1;
