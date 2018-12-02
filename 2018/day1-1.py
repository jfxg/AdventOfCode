#! /usr/bin/env python3.6

import aoc_common

def parse_int(value):
    try:
        return int(value)
    except ValueError:

        return float(s)

def main():
    args = aoc_common.parse_aoc_args()
    lines = aoc_common.open_file_lines(args.input)

    total = 0
    for line in lines:
        prev = total
        total += int(line)
        print("'{}' + '{}' = '{}'".format(prev, line, total))

    print ("Final total: {}".format(total))

main()
