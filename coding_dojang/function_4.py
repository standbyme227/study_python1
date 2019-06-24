def personal_info(name, age, address):
    print("이름: ", name)
    print("나이: ", age)
    print("주소: ", address)


x = {"name": "ssss", "age": 44, "address": "seoul"}
personal_info(**x)


def personal_info2(**kwargs):
    for key, value in kwargs.items():
        print(key, ": ", value, sep=" ")


def personal_info3(**kwargs):
    if "name" in kwargs:
        print("이름: ", kwargs["name"])
    if "age" in kwargs:
        print("나이: ", kwargs["age"])
    if "address" in kwargs:
        print("주소: ", kwargs["address"])
