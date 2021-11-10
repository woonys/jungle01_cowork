max_num = -987654321
index =0
li = []

for _ in range(9):
    li.append(int(input()))


print(max(li))
print(li.index(max(li))+1)
        