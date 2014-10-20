#!/usr/bin/python3
import argparse

import files

def parse(directory):
    exerciseFolders = directory.getSubDirs()
    for subDir in exerciseFolders:
        print(subDir.getFilename())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parse", action="store_true",
                                help="Parse exercises")
    parser.add_argument("dir", help="Root directory of exercices")
    parser.add_argument("-v", "--verbose", action="store_true",
                                help="increase output verbosity")
    args = parser.parse_args()
    if args.parse:
        print("Parsing {directory}...".format(directory = args.dir))
        parentDir = files.File(args.dir)
        parse(parentDir)
    else:
        print("Not parsing")

if __name__ == '__main__':
    main()
