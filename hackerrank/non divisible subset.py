#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
def nonDivisibleSubset(k, s):
    remainders = [x % k for x in s]
    hashmap = {}
    for i in remainders:
        hashmap[i] = 1 + hashmap.get(i, 0)

    ans = 0
    keys = list(hashmap.keys())

    while keys:
        a = keys[0]
        if a == 0 or k == a + a:
            ans += 1
        elif k - a in keys:
            ans += max(hashmap[a], hashmap[k - a])
        else:
            ans += hashmap[a]
        keys = [x for x in keys if x not in [a, k - a]]

    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
