n = int(input())
a = 0
b = 1
if n >= a:
    print(a)
while n >= b:
    print(b)
    c = b
    b = a + b
    a = c


