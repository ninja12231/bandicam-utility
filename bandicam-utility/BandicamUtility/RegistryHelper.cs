using Microsoft.Win32;

namespace BandicamUtility
{
    public static class RegistryHelper
    {
        public static bool IsTrialActive()
        {
            using var key = Registry.CurrentUser.OpenSubKey(@"Software\Bandicam");
            if (key == null)
                return false;

            var val = key.GetValue("TrialDaysLeft");
            return val != null && (int)val > 0;
        }

        public static void ResetTrial()
        {
            using var key = Registry.CurrentUser.CreateSubKey(@"Software\Bandicam");
            key.SetValue("TrialDaysLeft", 30);
            key.SetValue("FirstRun", 0);
        }
    }
}