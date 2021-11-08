from sys import stdin

# 2 < n <= 10000
# a = int(stdin.readline())
# li = []
# for i in range(a):
#     t = int(stdin.readline())
#     li.append(t)
#
# # prime list
# def is_prime(x):
#     if x == 1:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
#
# def prime_list(x):
#     p_li = []
#     for i in range(2, x):
#         if is_prime(i):
#             p_li.append(i)
#     return p_li
#
#
# for i in li:
#     print(i)
#     ans_list = []
#     for j in prime_list(i):
#         print(prime_list(i))
#         if (i - j) in prime_list(i):
#             t = [j, i - j]
#             t.sort()
#             if t in ans_list:
#                 continue
#             else:
#                 ans_list.append(t)
#
#             if len(ans_list) > 1:
#                 temp = []
#                 for i in ans_list:
#                     temp.append(abs(i[0] - i[1]))
#                 #print(ans_list[temp.index(min(temp))])


from sys import stdin

n = int(stdin.readline())
li = []
for i in range(n):
    a = int(stdin.readline())
    li.append(a)

def prime_list(x): #x보다 작은 소수 집합을 리스트로 반환
    temp_li = []
    if x == 1:
        return []

    for i in range(2, x):
        if i == 2:
            temp_li.append(i)
        elif i % 2 == 0:
            continue
        else:
            for j in range(2, i):
                if i % j != 0:
                    continue
                else:
                    break
            temp_li.append(i)
    return temp_li

def partition(x):
    primeList = prime_list(x)
    part_list = []
    for i in primeList:
        if (x-i) in primeList:
            temp = [i, x-i]
            temp.sort()
            if temp in part_list:
                continue
            else:
                part_list.append(temp)
    diff_list = []
    for i in part_list:
        i1, i2 = i[0], i[1]
        diff = abs(i1-i2)
        diff_list.append(diff)

    mi = min(diff_list)
    min_index = diff_list.index(mi)
    prime1, prime2 = part_list[min_index][0], part_list[min_index][1]
    return f'{prime1} {prime2}'

for i in li:
    print(partition(i))
