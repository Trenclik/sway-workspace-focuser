#!/usr/bin/env python3

import os

from i3ipc import Connection, Event

def temp_dir():
    return os.getenv("TMPDIR") or os.getenv("TEMP") or os.getenv("TMP") or "/tmp"


def wiggle(con):

    pass

def main():
    i3 = Connection()
    i3.main()


if __name__ == "__main__":
    main()
