#!/usr/bin/env python3

import sys
with open(sys.argv[2], 'w') as fo:
    for l in open(sys.argv[1]):
        arr = l.split(',')
        fo.write(f'{arr[0]}')
        for i in range(len(arr) - 1):
            fo.write(' %d:%s' % (i, arr[i+1]))
