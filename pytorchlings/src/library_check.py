"""Library availability detection for PyTorchlings"""

import importlib
import sys
from typing import Dict, Set


class LibraryChecker:
    """Check which optional libraries are available"""

    def __init__(self):
        self._cache: Dict[str, bool] = {}

    def is_available(self, library: str) -> bool:
        """Check if a library is importable"""
        if library in self._cache:
            return self._cache[library]

        try:
            importlib.import_module(library)
            self._cache[library] = True
            return True
        except ImportError:
            self._cache[library] = False
            return False

    def check_all(self) -> Dict[str, bool]:
        """Check all known libraries"""
        libraries = [
            'torch',
            'torchvision',
            'torchaudio',
            'pytorch_lightning',
            'transformers',
            'datasets',
            'torch_geometric',
            'watchdog',
        ]

        return {lib: self.is_available(lib) for lib in libraries}

    def get_missing_for_exercise(self, requires: Set[str]) -> Set[str]:
        """Get missing libraries for an exercise"""
        return {lib for lib in requires if not self.is_available(lib)}

    def can_run_exercise(self, requires: Set[str]) -> bool:
        """Check if all required libraries are available"""
        return len(self.get_missing_for_exercise(requires)) == 0

    def get_termux_compatible_status(self) -> Dict[str, str]:
        """Get Termux compatibility status for each library"""
        return {
            'torch': 'YES - Core library, works well',
            'torchvision': 'YES - Works well',
            'torchaudio': 'PARTIAL - May fail to install',
            'pytorch_lightning': 'PARTIAL - Many dependencies',
            'transformers': 'YES - But large downloads',
            'datasets': 'YES - But large downloads',
            'torch_geometric': 'NO - Requires C++ compilation',
            'watchdog': 'YES - Works well',
        }

    def print_status(self):
        """Print library availability status"""
        print("PyTorchlings Library Status")
        print("=" * 60)

        availability = self.check_all()

        # Core libraries
        print("\nCore Libraries:")
        for lib in ['torch', 'torchvision']:
            status = "✓ Available" if availability[lib] else "✗ Not installed"
            print(f"  {lib:<20} {status}")

        # Optional libraries
        print("\nOptional Libraries:")
        for lib in ['torchaudio', 'pytorch_lightning', 'transformers', 'datasets', 'torch_geometric', 'watchdog']:
            status = "✓ Available" if availability[lib] else "✗ Not installed"
            print(f"  {lib:<20} {status}")

        # Summary
        available_count = sum(availability.values())
        total_count = len(availability)
        print(f"\nTotal: {available_count}/{total_count} libraries available")

        # Recommendations
        if not availability['torch']:
            print("\n⚠️  PyTorch not installed - most exercises will be skipped")
            print("   Install with: pip install torch torchvision")
        elif available_count < 4:
            print(f"\n💡 {total_count - available_count} optional libraries not installed")
            print("   This is fine! The framework will skip exercises requiring them.")
            print("   See requirements.txt for installation profiles.")

    def get_installation_profile(self) -> str:
        """Determine which installation profile is active"""
        availability = self.check_all()

        if not availability['torch']:
            return "minimal"
        elif availability['torch'] and availability['torchvision'] and not availability['torchaudio']:
            return "basic"
        elif availability['torchaudio'] and availability['transformers']:
            return "full"
        else:
            return "standard"


# Global instance
_checker = LibraryChecker()


def is_available(library: str) -> bool:
    """Check if a library is available (convenience function)"""
    return _checker.is_available(library)


def can_run_exercise(requires: Set[str]) -> bool:
    """Check if an exercise can run (convenience function)"""
    return _checker.can_run_exercise(requires)


def get_missing_libraries(requires: Set[str]) -> Set[str]:
    """Get missing libraries (convenience function)"""
    return _checker.get_missing_for_exercise(requires)


def print_library_status():
    """Print library status (convenience function)"""
    _checker.print_status()


def get_profile() -> str:
    """Get installation profile (convenience function)"""
    return _checker.get_installation_profile()
