import timeit


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


cache = {0: 0, 1: 1}


def fib2(n):
    if n in cache:
        return cache[n]
    else:
        f = fib2(n - 1) + fib2(n - 2)
        cache[n] = f
        return f


# for n in [10, 20, 30]:
#     t_reg = timeit.Timer(lambda: fib(n)).repeat(number=1, repeat=1)[0]
#     t_mem = timeit.Timer(lambda: fib2(n)).repeat(number=1, repeat=1)[0]
#     print(f'Скорость для n={n} :')
#     print(f'Обычный Fibo {t_reg:.5g} секунд, мемоизированный fibo {t_mem:.5g} секунд')
#     print(f'Мемоизированный  fibo быстрее примерно в {t_reg/t_mem:.3f} раз')

fib1 = fib2 = 1

n = int(input('Введите значение n: '))

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ***')
