n = int(input())
a = 0
b = 1
print(a)
print(b)
while n >= b:
    c = b
    b = a + b
    a = c
    print(b)

