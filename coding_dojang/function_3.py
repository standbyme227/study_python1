def personal_info(name, age, address):
    print("이름: ", name)
    print("나이: ", age)
    print("주소: ", address)


# 키워드 인수
# 파이썬에서는 인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수(keyword argument)라는 기능을 제공


x = {"name": "신종민", "age": 33, "address": "서울"}
personal_info(**x)
