# Lab 07 Task 02: Command Line Arguments with argparse
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Basic argparse example')
    parser.add_argument('name', nargs='?', default='World', help='Your name')
    args = parser.parse_args()
    print(f'Hello, {args.name}!')
