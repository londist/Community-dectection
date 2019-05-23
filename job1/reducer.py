

#!/usr/bin/env python

import sys

currentKey = None
thisKey = None
currentCount = 0

for line in sys.stdin:
    thisKey, thisCount = line.strip().split('\t', 1)
    try:
        thisCount = int(thisCount)
    except ValueError:
        continue
    if currentKey == thisKey:
        currentCount += thisCount
    else:
        if currentKey:
            print('{0}\t{1}'.format(currentKey,currentCount))
            currentCount = thisCount
        else:
            currentCount = thisCount
        currentKey = thisKey


print('{0}\t{1}'.format(currentKey,currentCount))