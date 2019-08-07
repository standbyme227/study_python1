def outer_func(name, age):
    name = name
    age = age

    def inner_func():
        print(f"my name is {name}, and i am {age} years old")

    return inner_func


inner = outer_func("swut", "29")
inner()

print(of.__closure__[0].cell_contents)
print(of.__closure__[1].cell_contents)