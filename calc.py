#!/usr/bin/env python
from __future__ import print_function
import sys
import commands

if __name__ == "__main__":
    command_name = sys.argv[1]
    try:
        command = getattr(commands, 'command_' + command_name)
    except AttributeError:
        print("Error: unrecognised command", file=sys.stderr)
        sys.exit(-1)
    try:
        args = (int(x) for x in sys.argv[2:])
    except ValueError:
        print("Error: arguments should be numeric", file=sys.stderr)
        sys.exit(-1)
    print(command(*args))
