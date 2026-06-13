"""Bandicam Utility - Unofficial Bandicam license management tool."""

__version__ = "1.0.0"
__author__ = "Bandicam Utility Team"

from .core import BandicamUnlocker
from .license import LicenseManager

__all__ = ["BandicamUnlocker", "LicenseManager"]