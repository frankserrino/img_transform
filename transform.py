"""
Created on Mon Aug 22 19:51:38 2016,
modified and expanded upon from https://gist.github.com/vinu76jsr/8594481
"""

import os
from path import path
import argparse
from transforming_file_function import transform_file


def transform(source_dir, dest_dir):
    file_count = 0
    for i in source_dir.walk():
        if i.isfile():# and i.endswith('txt'):
            file_count += 1
            i.copy(dest_dir)  
            print "Transforming %s" % i
    print 'Transformed %s files' % file_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    print 'test'
    parser.add_argument("--source", help="the input directory of images")
    parser.add_argument("--dest", help="the destination directory of the transformed images")
    args = parser.parse_args()
    SOURCE_DIRECTORY =  args.source
    DEST_DIRECTORY = args.dest    
    source = path(SOURCE_DIRECTORY)
    dest = path(DEST_DIRECTORY)
    #   print "Transforming files from %s to %s" % (source_dir, dest_dir)
    print 'test2'
    transform(source, dest)

