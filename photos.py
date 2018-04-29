#! /usr/bin/python

import os,sys
from datetime import datetime
import time
import shutil
import exifread



if len(sys.argv) >= 2:
    dir = sys.argv[1]
else:
    dir = "."
if len(sys.argv) >= 3:
    dest = sys.argv[2]
else:
    dest = ".."

# Initialize files dict
files = {}

# List all files in the directory
for file in os.listdir(dir):
    f = "{}{}".format(dir,file)
    # Open image file for reading (binary mode)
    with open(f, 'rb') as fh:
        tags = exifread.process_file(fh)
    try:
    	origin = str(tags['EXIF DateTimeOriginal']).split()[0]
    	mtime = origin.replace(':','-')
    # If the DateTimeOriginal key doesn't exist we couldn't get
    # the exif data, so we'll just use last modified time as
    # the creation time.  It's as accurate as we can get.
    except KeyError:
        epoch = os.path.getmtime(f)
        mtime = time.strftime('%Y-%m-%d', time.localtime(epoch))
    if not mtime in files:
      	files[mtime] = []
    files[mtime].append(file)

for key in files:
    for index,file in enumerate(files[key]):
        extension = file.split('.')[-1].lower()
        dst = "{}/{} {}.{}".format(dest, key, index, extension)
        src = "{}{}".format(dir, file)
        print "SRC: {}, DEST: {}".format(src, dst)

        # Open the file and raise an exception if it exists
        fd = os.open(dst, os.O_CREAT | os.O_EXCL | os.O_WRONLY)

        shutil.copyfile(src, dst)
