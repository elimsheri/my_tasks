def num_feban(n):
    a = 0
    b = 1
    if n >= a:
        print(a, end=' ')
    while n >= b:
        print(b, end=' ')
        c = b
        b = a + b
        a = c
print('Вывод чисел Фибоначи до указнного значения')
n = int(input('Укажите предельное значение '))
num_feban(n)




