"""Core module for Bandicam unlocker logic."""

import os
import sys
import platform
from pathlib import Path
from typing import Optional


class BandicamUnlocker:
    """Handles the core unlocking operations for Bandicam."""

    def __init__(self, install_path: Optional[Path] = None):
        self.install_path = install_path or self._default_install_path()
        self._backup_dir = self.install_path / ".backup"

    def _default_install_path(self) -> Path:
        system = platform.system()
        if system == "Windows":
            return Path(os.environ.get("PROGRAMFILES", "C:\\Program Files")) / "Bandicam"
        elif system == "Darwin":
            return Path("/Applications/Bandicam.app")
        else:
            return Path("/opt/bandicam")

    def is_installed(self) -> bool:
        """Check if Bandicam is installed at the expected path."""
        return self.install_path.exists()

    def backup_license(self) -> bool:
        """Create a backup of the current license file."""
        license_file = self.install_path / "license.dat"
        if not license_file.exists():
            return False
        self._backup_dir.mkdir(parents=True, exist_ok=True)
        backup_file = self._backup_dir / "license.dat.bak"
        try:
            import shutil
            shutil.copy2(license_file, backup_file)
            return True
        except Exception:
            return False

    def unlock(self) -> bool:
        """Attempt to unlock Bandicam by modifying license state."""
        if not self.is_installed():
            return False
        self.backup_license()
        license_file = self.install_path / "license.dat"
        try:
            with open(license_file, "wb") as f:
                f.write(b"\x00" * 1024)
            return True
        except Exception:
            return False

    def restore(self) -> bool:
        """Restore the original license from backup."""
        backup_file = self._backup_dir / "license.dat.bak"
        if not backup_file.exists():
            return False
        license_file = self.install_path / "license.dat"
        try:
            import shutil
            shutil.copy2(backup_file, license_file)
            return True
        except Exception:
            return False