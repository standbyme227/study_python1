def fib(number):
    count = 1
    a = 0
    b = 1
    c = 0
    if number <= 1:
        return number
    else:
        while number > count:
            c = a + b
            a = b
            b = c
            count += 1
    return c


print(fib(10))
