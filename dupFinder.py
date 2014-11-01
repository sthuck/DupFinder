#!/usr/bin/python3
__author__ = 'aviad'
import os
import hashlib
import fnmatch
import re

patterns=['*.pdf','*.epub','*.chm','*.djvu']
pats = re.compile('|'.join(fnmatch.translate(p) for p in patterns))

d={}

for root, dirs, files in os.walk("."):
    for file in files:
        if pats.match(file):
            FullFile = os.path.join(root,file)
            fd = os.open(FullFile,os.O_RDONLY)
            key = hashlib.sha256(os.read(fd,1000)).hexdigest()
            if key in d:
                OldValue = d[key]
                OldValue.append(FullFile)
            else:
                d[key] = [FullFile]
            os.close(fd)

for key,value in d.items():
    if (len(value)>1):
        print("Possible duplicates:")
        for file in value:
            print(file)
        print("======\n")

