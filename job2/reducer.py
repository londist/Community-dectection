#!/usr/bin/env python

import sys

currentKey = None
result = ''
currentSimilar = []

def get_count(value):
    return value[1]

for line in sys.stdin:
    key1, key2, count = line.strip().split('\t', 2)
    try:
        count = int(count)
    except ValueError:
        continue
    if currentKey == key1:
        currentSimilar.append((key2, count))
    else:
        if currentKey:
            currentSimilar = sorted(currentSimilar, key = get_count, reverse = True)
            for item in currentSimilar[0:10]:
                result += item[0] + ' '
            print('{0}:{1}'.format(currentKey, result))
            result = ''
        currentKey = key1
        currentSimilar = [(key2, count)]

#输出最后一项
currentSimilar = sorted(currentSimilar, key=get_count)
for item in currentSimilar[0:10]:
    result += item[0] + ' '
print('{0}:{1}'.format(currentKey, result))