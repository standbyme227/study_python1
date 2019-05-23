# import turtle as t
#
# t.shape("turtle")
# t.circle(120)
#
# t.mainloop()

# import turtle as t
#
# n = int(input())
# t.shape("turtle")
# t.speed("fastest")
#
# for i in range(n):
#     t.circle(120)
#     t.right(360 / n)


import turtle as t

t.shape("turtle")
t.speed("fastest")

for i in range(300):
    t.forward(i)
    t.right(91)

t.mainloop()
