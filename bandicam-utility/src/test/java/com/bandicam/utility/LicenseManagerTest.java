package com.bandicam.utility;

import org.junit.jupiter.api.*;
import java.io.IOException;
import java.nio.file.*;

import static org.junit.jupiter.api.Assertions.*;

class LicenseManagerTest {

    private Path tempFile;
    private LicenseManager manager;

    @BeforeEach
    void setUp() throws IOException {
        tempFile = Files.createTempFile("license", ".txt");
        manager = new LicenseManager(tempFile);
    }

    @AfterEach
    void tearDown() throws IOException {
        Files.deleteIfExists(tempFile);
    }

    @Test
    void testUnlockAndValidate() throws IOException {
        assertFalse(manager.isLicenseValid());
        manager.unlock();
        assertTrue(manager.isLicenseValid());
    }

    @Test
    void testLock() throws IOException {
        manager.unlock();
        manager.lock();
        assertFalse(manager.isLicenseValid());
    }
}