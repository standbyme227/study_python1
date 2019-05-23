import turtle as t

n = int(input())

t.shape("turtle")
# t.color("blue")
# t.begin_fill()
for i in range(n):
    t.fd(40)
    t.rt(360/n)
# t.end_fill()

t.mainloop()
