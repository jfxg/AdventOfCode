import argparse

def open_file_lines(path):
    return [line.rstrip('\n') for line in open(path)]

def parse_aoc_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    return parser.parse_args()
