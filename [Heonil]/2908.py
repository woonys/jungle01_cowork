# 거꾸로 읽고  더 큰수를 이야기 한다.
# python도 reverse가 있는가?

a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

print(max(a,b))

