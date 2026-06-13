package com.bandicam.utility;

import java.io.*;
import java.nio.file.*;
import java.util.*;

public class LicenseManager {

    private final Path licenseFile;

    public LicenseManager(Path licenseFile) {
        this.licenseFile = licenseFile;
    }

    public boolean isLicenseValid() {
        if (!Files.exists(licenseFile)) return false;
        try {
            String content = Files.readString(licenseFile).trim();
            return content.equals("UNLOCKED");
        } catch (IOException e) {
            return false;
        }
    }

    public void unlock() throws IOException {
        Files.writeString(licenseFile, "UNLOCKED");
    }

    public void lock() throws IOException {
        Files.writeString(licenseFile, "LOCKED");
    }
}