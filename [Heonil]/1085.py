x, y, w, h= map(int, input().split())


a = min(y, h-y)
b = min(x, w-x)

print(min(a,b))
