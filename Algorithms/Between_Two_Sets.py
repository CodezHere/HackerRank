'''
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
a = [2,6]
b = [24,36]

There are two numbers between the arrays: 6 and 12.
6%2 = 0, 6%6 = 0, 24%6 = 0 and 36%6 = 0 for the first value.
12%2 = 0, 12%6 = 0 and 24%12 = 0, 36%12 = 0 for the second value. Return 2.

Function Description

Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):
int a[n]: an array of integers
int b[m]: an array of integers

Returns
int: the number of integers that are between the sets

Input Format
The first line contains two space-separated integers,  and , the number of elements in arrays  and .
The second line contains  distinct space-separated integers  where .
The third line contains  distinct space-separated integers  where .

Constraints
- 1<= n, m<=10
- 1 <= a[i] <=100
- 1 <= b[j] <= 100

Sample Input
2 3
2 4
16 32 96

Sample Output
3

Explanation
2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.
'''

!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)
    count = 0

    for i in range(max_a, min_b + 1):
        if all(i % factor == 0 for factor in a) and all(factor % i == 0 for factor in b):
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()