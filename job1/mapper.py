#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split(':')
    followers = line[1].split(' ')
    i = 0 
    for follower1 in followers:
        for follower2 in followers[i + 1:]:
            if follower1 > follower2:
                print('{0}-{1}\t{2}'.format(follower2, follower1, 1))
            else:
                print('{0}-{1}\t{2}'.format(follower1, follower2, 1))
        i = i + 1
