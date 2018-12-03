#! /usr/bin/env python3.6

import aoc_common

def analyze(line):
    results = {
        'doubles': False,
        'triples': False,
        'counts': {}
    }

    last = ' '
    for char in sorted(line):
        if char == last:
            results['counts'][char] += 1
        else:
            results['counts'][char] = 1
        last = char

    results['doubles'] = any(x == 2 for x in results['counts'].values())
    results['triples'] = any(x == 3 for x in results['counts'].values())

    print("Results for '{}': {}".format(line, results))
    return results

def main():
    args = aoc_common.parse_aoc_args()
    lines = aoc_common.open_file_lines(args.input)

    doublesCount = 0
    triplesCount = 0

    for line in lines:
        stats = analyze(line)
        if stats['doubles']:
            doublesCount += 1
        if stats['triples']:
            triplesCount += 1

    checkSum = doublesCount * triplesCount
    print("Final Checksum: doubles:{} * triples:{} = checksum:{}".format(doublesCount, triplesCount, checkSum))

main()
