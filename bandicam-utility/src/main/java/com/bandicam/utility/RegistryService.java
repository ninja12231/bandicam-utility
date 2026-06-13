package com.bandicam.utility;

import java.util.prefs.Preferences;

public class RegistryService {

    private static final String KEY_TRIAL_USED = "trialUsed";

    public boolean hasTrialBeenUsed() {
        Preferences prefs = Preferences.userRoot().node("Bandicam");
        return prefs.getBoolean(KEY_TRIAL_USED, false);
    }

    public void resetTrial() {
        Preferences prefs = Preferences.userRoot().node("Bandicam");
        prefs.putBoolean(KEY_TRIAL_USED, false);
        prefs.putLong("trialStartTime", 0L);
    }
}