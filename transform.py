"""
Created on Mon Aug 22 19:51:38 2016
based on https://gist.github.com/vinu76jsr/8594481
"""

import os
from path import path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("SOURCE")
parser.add_argument("DEST")
args = parser.parse_args()
SOURCE_DIRECTORY =  args.SOURCE
DEST_DIRECTORY = args.DEST
  
d = path(SOURCE_DIRECTORY)
dest_directory = path(DEST_DIRECTORY)

def transform():
    print "Transforming files from %s to %s" % (d, dest_directory)
    file_count = 0
    for i in d.walk():
        if i.isfile() and i.endswith('txt'):
            file_count += 1
            print "Transforming %s" % i

# ***  between this comment and the one below is the place we place our transformation code

            i.copy(dest_directory)

# ***

    print 'Transformed %s files' % file_count


if __name__ == "__main__":
    transform()

