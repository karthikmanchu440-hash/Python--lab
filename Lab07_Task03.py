# Lab 07 Task 03: argparse with flags
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Argparse flags example')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    if args.verbose:
        print('Verbose mode is enabled.')
    else:
        print('Verbose mode is disabled.')
