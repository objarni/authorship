#!/usr/bin/env python
import os
import re
import sys
from collections import defaultdict
import subprocess

email_re = re.compile(r'<.*?>')
devnull = open(os.devnull, 'w')


def git_blame(path):
    process = subprocess.Popen(['git', 'blame', '-e', path], stdout=subprocess.PIPE, stderr=devnull)
    out, err = process.communicate()
    return out.splitlines()


def analyse(exts):
    author_line_count = defaultdict(lambda: 0)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            ext = os.path.splitext(name)[1]
            if ext in exts:
                for row in git_blame(os.path.join(root, name)):
                    m = email_re.search(str(row))
                    if m:
                        email = m.group(0)
                        author_line_count[email] += 1
    return author_line_count


def sorter(kv):
    (k, v) = kv
    return (-v,k)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please add .py .cpp or whatever files you are interested in!")
    else:
        d = analyse(sys.argv[1:])
        for key, value in sorted(d.items(), key=sorter):
            print("%s: %s" % (key, value))

