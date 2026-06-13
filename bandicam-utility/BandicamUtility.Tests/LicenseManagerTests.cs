using System;
using System.IO;
using Xunit;

namespace BandicamUtility.Tests
{
    public class LicenseManagerTests
    {
        [Fact]
        public void Unlock_CreatesLicenseFile()
        {
            string tempFile = Path.GetTempFileName();
            try
            {
                File.Delete(tempFile);
                var mgr = new LicenseManager(tempFile);
                bool result = mgr.Unlock();
                Assert.True(result);
                Assert.True(File.Exists(tempFile));
            }
            finally
            {
                if (File.Exists(tempFile))
                    File.Delete(tempFile);
            }
        }

        [Fact]
        public void IsLicensed_ReturnsTrueAfterUnlock()
        {
            string tempFile = Path.GetTempFileName();
            try
            {
                File.Delete(tempFile);
                var mgr = new LicenseManager(tempFile);
                mgr.Unlock();
                Assert.True(mgr.IsLicensed());
            }
            finally
            {
                if (File.Exists(tempFile))
                    File.Delete(tempFile);
            }
        }

        [Fact]
        public void RemoveLicense_DeletesFile()
        {
            string tempFile = Path.GetTempFileName();
            try
            {
                File.WriteAllText(tempFile, "test");
                var mgr = new LicenseManager(tempFile);
                bool removed = mgr.RemoveLicense();
                Assert.True(removed);
                Assert.False(File.Exists(tempFile));
            }
            finally
            {
                if (File.Exists(tempFile))
                    File.Delete(tempFile);
            }
        }
    }
}