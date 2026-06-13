using System;
using System.IO;
using System.Text;

namespace BandicamUtility
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bandicam Unlocker Utility v1.0");
            Console.WriteLine("-------------------------------");

            string bandicamPath = @"C:\Program Files\Bandicam";
            string licenseFile = Path.Combine(bandicamPath, "license.key");

            if (!Directory.Exists(bandicamPath))
            {
                Console.WriteLine("[!] Bandicam not found at default path.");
                Console.WriteLine("[*] Creating mock environment for testing...");
                Directory.CreateDirectory(bandicamPath);
            }

            if (File.Exists(licenseFile))
            {
                Console.WriteLine("[*] Existing license found. Removing...");
                File.Delete(licenseFile);
            }

            string fakeLicense = GenerateFakeLicense();
            File.WriteAllText(licenseFile, fakeLicense);
            Console.WriteLine("[+] Fake license written successfully.");
            Console.WriteLine("[*] Restart Bandicam to apply changes.");
        }

        static string GenerateFakeLicense()
        {
            var sb = new StringBuilder();
            sb.AppendLine("[LICENSE]");
            sb.AppendLine("Type=Unlimited");
            sb.AppendLine("Expiry=2099-12-31");
            sb.AppendLine("Key=" + Guid.NewGuid().ToString().ToUpper());
            return sb.ToString();
        }
    }
}