#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    try:
        with open('.env') as fp:
            for line in fp:
                k, v = line.strip().split('=', 1)
                os.environ[k] = v
    except FileNotFoundError:
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
