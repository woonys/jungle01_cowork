import sys
#hi
a,b = map(int,sys.stdin.readline().split())

print(a+b, a-b, a*b, int(a/b), a%b, sep='\n')