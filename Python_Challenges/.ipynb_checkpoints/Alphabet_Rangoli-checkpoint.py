"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter
(in alphabetical order).

Function Description
Complete the rangoli function in the editor below.
rangoli has the following parameters:
int size: the size of the rangoli

Returns
string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

Input Format
Only one line of input containing , the size of the rangoli.

Constraints
0<size<27

Sample Input
5

Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

def print_rangoli(size):
    # your code goes here
    n = size
    lst1 = list(map(chr, range(97, 123)))
    x = lst1[n-1::-1]+lst1[1:n]
    m = len("-".join(x))
    for i in range(1,n):
        print("-".join(lst1[n-1:n-i:-1] + lst1[n-i:n]).center(m, "-"))
    for i in range(n, 0, -1):
        print("-".join(lst1[n-1:n-i:-1] + lst1[n-i:n]).center(m, "-"))


if __name__ == '__main__':