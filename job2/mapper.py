#!/usr/bin/env python

import sys

for line in sys.stdin:
    key, count = line.strip().split('\t',1)
    key1, key2 = key.split('-', 1)
    print('{0}\t{1}\t{2}'.format(key1, key2, count))
    print('{0}\t{1}\t{2}'.format(key2, key1, count))