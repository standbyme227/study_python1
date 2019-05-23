import turtle as t

n, line = map(int, input().split())
t.shape("turtle")
# t.speed("fastest")

total_degree = 180 * (n - 2)
a_degree = total_degree / n
out_degree = 2 * (180 - a_degree)
for i in range(n):
    t.fd(line)
    t.lt(180 - a_degree)
    t.fd(line)
    t.rt(out_degree)

t.mainloop()
