#!/usr/bin/python3
import sys

for arg in sys.argv[1:]:  # FIX: sys.argv[1:] excludes the script name
    print(arg)

