"""License management utilities for Bandicam."""

import hashlib
import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class LicenseInfo:
    """Represents Bandicam license information."""
    key: str
    email: str
    valid_until: int
    product: str = "Bandicam"


class LicenseManager:
    """Manages license validation and generation."""

    def __init__(self):
        self._licenses = {}

    def validate_key(self, key: str) -> bool:
        """Check if a license key has valid format."""
        if len(key) != 25:
            return False
        parts = key.split("-")
        if len(parts) != 5:
            return False
        for part in parts:
            if len(part) != 5 or not part.isalnum():
                return False
        return True

    def generate_trial_license(self, email: str) -> LicenseInfo:
        """Generate a fake trial license for testing purposes."""
        raw = f"{email}:{int(time.time())}:trial"
        key_part = hashlib.md5(raw.encode()).hexdigest()[:20]
        key = "-".join([key_part[i:i+5] for i in range(0, 20, 5)])
        license_info = LicenseInfo(
            key=key.upper(),
            email=email,
            valid_until=int(time.time()) + 86400 * 30,
        )
        self._licenses[email] = license_info
        return license_info

    def get_license(self, email: str) -> Optional[LicenseInfo]:
        """Retrieve stored license for a given email."""
        return self._licenses.get(email)