#!/usr/bin/env python
'''
Author: Michael Ricks-Aherne

Parses a text file with lines that say either 'starting <something>' or
'finishing <something>', and emits all <something>'s that were started but not
finished.

USAGE:
    parser.py example.txt

EXAMPLE:
    If the file contains:

    starting task A
    starting task B
    finishing task B
    starting task C
    starting task D
    finishing task A

    The program will emit:

    task C
    task D
'''
import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        help="Text file name")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    aFile = read(args.file)
    results = parse(aFile)
    for result in results:
        print result


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


def parse(text):
    starts = re.findall('^starting (.*)', text, flags=re.MULTILINE)
    finishes = re.findall('^finishing (.*)', text, flags=re.MULTILINE)
    diff = list(set(starts) - set(finishes))
    return diff

if __name__ == '__main__':
    main()
