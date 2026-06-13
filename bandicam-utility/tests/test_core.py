"""Tests for the core module."""

import unittest
from pathlib import Path
from unittest.mock import patch
from bandicam_utility.core import BandicamUnlocker


class TestBandicamUnlocker(unittest.TestCase):
    """Test suite for BandicamUnlocker."""

    def setUp(self):
        self.unlocker = BandicamUnlocker(install_path=Path("/fake/bandicam"))

    def test_is_installed_false(self):
        self.assertFalse(self.unlocker.is_installed())

    @patch("bandicam_utility.core.Path.exists")
    def test_is_installed_true(self, mock_exists):
        mock_exists.return_value = True
        self.assertTrue(self.unlocker.is_installed())

    def test_unlock_fails_when_not_installed(self):
        result = self.unlocker.unlock()
        self.assertFalse(result)

    @patch("bandicam_utility.core.BandicamUnlocker.is_installed")
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_unlock_success(self, mock_open, mock_installed):
        mock_installed.return_value = True
        result = self.unlocker.unlock()
        self.assertTrue(result)
        mock_open.assert_called_once()

    def test_restore_no_backup(self):
        result = self.unlocker.restore()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()