def hello(count):
    if count == 0:
        return
    print("Hello, world", count)

    count -= 1
    hello(count)


hello_cnt = input()

try:
    hello_cnt = int(hello_cnt)
except:
    print("Have to input the int value")
    exit()

hello(hello_cnt)
