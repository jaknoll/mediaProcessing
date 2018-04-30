#! /usr/bin/python
'''
    Organize pictures and movies by year/month

    ARGS:   Directory to process
            Pictures Destination
            Movies Destination
'''

import argparse
import os
import sys

def parse_args():

    parser = argparse.ArgumentParser(description='Organize Picture/Video files' +
            ' by month/year')
    parser.add_argument('-d', '--directory', type=str,
                                help='Directory to parse', required=True)
    parser.add_argument('-p', '--pictures', type=str,
                                help='Destination for pictures', required=True)
    parser.add_argument('-m', '--movies', type=str,
                                help='Destination for movies', required=True)

    args = parser.parse_args()
    return args

def main(args):
    pics = args.pictures
    movies = args.movies
    source = args.directory
    pass

if __name__ == '__main__':
    args = parse_args()
    main(args)
