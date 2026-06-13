using System;
using System.IO;

namespace BandicamUtility
{
    public class LicenseManager
    {
        private readonly string _licensePath;

        public LicenseManager(string licensePath)
        {
            _licensePath = licensePath;
        }

        public bool IsLicensed()
        {
            if (!File.Exists(_licensePath))
                return false;

            string content = File.ReadAllText(_licensePath);
            return content.Contains("Type=Unlimited");
        }

        public bool Unlock()
        {
            try
            {
                string dir = Path.GetDirectoryName(_licensePath);
                if (!Directory.Exists(dir))
                    Directory.CreateDirectory(dir);

                string fakeLicense = $"[LICENSE]\nType=Unlimited\nExpiry=2099-12-31\nKey={Guid.NewGuid().ToString().ToUpper()}\n";
                File.WriteAllText(_licensePath, fakeLicense);
                return true;
            }
            catch
            {
                return false;
            }
        }

        public bool RemoveLicense()
        {
            if (!File.Exists(_licensePath))
                return false;

            File.Delete(_licensePath);
            return true;
        }
    }
}