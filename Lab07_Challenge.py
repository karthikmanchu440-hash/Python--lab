# Lab 07 Challenge: argparse with --help functionality
import argparse
def main():
    parser = argparse.ArgumentParser(description='A complete argparse tool with --help support.')
    parser.add_argument('--input', type=str, help='Input file path')
    parser.add_argument('--output', type=str, help='Output file path')
    args = parser.parse_args()
    if args.input and args.output:
        print(f'Processing from {args.input} to {args.output}')
    else:
        print('Run with --help to see usage instructions.')
if __name__ == '__main__':
    main()
