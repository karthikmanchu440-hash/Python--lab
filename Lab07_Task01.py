# Lab 07 Task 01: Command Line Arguments with sys.argv
import sys
if len(sys.argv) > 1:
    print('Arguments passed:', sys.argv[1:])
else:
    print('No arguments provided.')
