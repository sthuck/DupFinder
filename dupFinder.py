#!/usr/bin/python3
__author__ = 'aviad'
import os
import hashlib
import fnmatch
import re
import sys

patterns=['*.pdf','*.epub','*.chm','*.djvu']
pats = re.compile('|'.join(fnmatch.translate(p) for p in patterns))

d={}

def main():
    dirs = []
    if len(sys.argv) == 1:
        print("Usage:DupFinder [folder1] [folder2] ...")
        sys.exit(-1)
    dirs = sys.argv
    dirs.pop(0);

    for dir in dirs:
        print("Scanning dir:" + dir)
        for root, dirs, files in os.walk(dir):
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


if __name__ == "__main__": main()