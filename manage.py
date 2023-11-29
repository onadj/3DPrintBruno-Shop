
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import platform

# Check if the platform is Windows
if platform.system() == "Windows":
    try:
        # Attempt to import pywin32
        import pywin32
    except ImportError:
        # Handle the case where pywin32 is not available on non-Windows platforms
        pywin32 = None
else:
    # Set pywin32 to None for non-Windows platforms
    pywin32 = None

# Now you can use pywin32 if it's available (and you're on Windows)
if pywin32:
    # Your Windows-specific code using pywin32
    pass
else:
    # Handle the case where pywin32 is not available on non-Windows platforms
    pass

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greatkart.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
