package com.bandicam.utility;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class MainUnlocker {

    public static void main(String[] args) {
        Path licensePath = Paths.get(System.getProperty("user.home"), ".bandicam_license");
        LicenseManager manager = new LicenseManager(licensePath);
        RegistryService registry = new RegistryService();

        try {
            if (!manager.isLicenseValid()) {
                manager.unlock();
                registry.resetTrial();
                System.out.println("Bandicam unlocked successfully.");
            } else {
                System.out.println("Bandicam is already unlocked.");
            }
        } catch (IOException e) {
            System.err.println("Failed to unlock Bandicam: " + e.getMessage());
        }
    }
}