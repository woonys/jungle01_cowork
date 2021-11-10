from itertools import permutations
from sys import stdin
from typing import MutableSequence

num = int(stdin.readline())
li = map(int, stdin.readline().split())

for i in permutations(li, num):
    for j in range(num):
        print(i[j])