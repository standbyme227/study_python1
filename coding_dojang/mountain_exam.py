# h = int(input())
#
# w = h * 2
# for i in range(h):
#     for j in range(w):
#         # print(j, end='')
#         # if i == h:
#         #     print("*", end='')
#         if j < h - i:
#             print(end=" ")
#         elif j >= h - i and j <= h + i:
#             # for k in range((i * 2) + 1):
#             print("*", end='')
#     print()

h = int(input())

w = h * 2
for i in range(h):
    for j in range(w):
        if j < h - i - 1:
            print(end=" ")
        elif j >= h - i - 1 and j <= h + i - 1:
            print("*", end='')
        elif j > h + i - 1:
            break
    print()


# join을 쓰면 되겠다.
