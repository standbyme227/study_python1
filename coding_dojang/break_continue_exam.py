start, stop = map(int, input().split())
i = start
while True:
    if int(list(str(i))[-1]) == 3:
        i += 1
        continue
    elif i > stop:
        break
    print(i, end=' ')
    i += 1