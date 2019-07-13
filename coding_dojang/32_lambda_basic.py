def plus_ten(x):
    return x + 10


plus_ten2 = lambda x: x + 10


list(map(plus_ten, [1,2,3]))

list(map(lambda x: x+10, [1,2,3]))