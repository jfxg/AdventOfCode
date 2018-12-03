#! /usr/bin/env python3.6

import aoc_common

def different_chars(line1, line2):
    differ = 0
    for a,b in zip(line1, line2):
        if a != b:
            differ += 1
    return differ

def main():
    args = aoc_common.parse_aoc_args()
    lines = aoc_common.open_file_lines(args.input)

    # Sort lines to look for 1-off differences
    sortedLines = sorted(lines)

    last = ""
    lineNum = 0
    for line in sortedLines:
        differ = different_chars(last, line)
        if (differ == 1):
            print ("{:03d} {} (*****{}*****)".format(lineNum, line, differ))
        else:
            print ("{:03d} {}".format(lineNum, line))
        last = line
        lineNum += 1

main()
