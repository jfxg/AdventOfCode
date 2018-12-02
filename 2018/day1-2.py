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

    seen = {}
    count = 0
    frequency = 0
    while True:
        for line in lines:
            count += 1
            if frequency in seen:
                print("Seen frequency '{}' twice!".format(frequency))
                return
            else:
                seen[frequency] = 1

            prev = frequency
            frequency += int(line)
            print("[{:09d}] '{}' + '{}' = '{}'".format(count, prev, line, frequency))

main()
