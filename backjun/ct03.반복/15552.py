# input 대신 sys.stdin.readline - 빠르게
import sys
n, lst = int(input('')), list()
for i in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    sum = a + b
    lst.append(sum)
for i in lst:
    print(i)
