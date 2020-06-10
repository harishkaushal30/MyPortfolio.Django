#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import my_portfolio.settings

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_portfolio.settings')
    if os.path.exists("keys.py"):
        import keys
    else:
        print("keys file doesn't exits..")
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
