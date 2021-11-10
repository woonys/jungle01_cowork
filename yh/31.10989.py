from sys import _WinVersion, stdin
rpt = int(stdin.readline())
i = 0
li = [0] * 10000

for _ in range(rpt) :
     li[int(stdin.readline())] += 1

for i in range(10001):
     for j in li :
          while j > 0 :
               print(i)
               j -= 1
          else:
               break
