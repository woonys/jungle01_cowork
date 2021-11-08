a= int(input())
b = int(input())
a = int(a)
b = int(b)

c = b

for _ in range(3):
    temp = b%10
    print(temp*a)
    b = int(b/10)
print(a*c)