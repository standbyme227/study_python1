print(10, 20, 30)


def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


# 언패킹
# 인수를 순서대로 넣을 때는 리스트나 튜플을 사용할 수도 있음
# 다음과 같이 리스트 또는 튜플 앞에 *(애스터리스크)를 붙여서 함수에 넣어주면 됨

x = [19, 29, 39]

print_numbers(*x)


# 위치 인수와 리스트 어ㄴ패킹은 인수의 개수가 정해지지 않은 가변 인수(variable argument)에 사용함
# 다음과 같이 가변 인수 함수는 매개변수 아페 *를 붙여서 만듬.

def print_numbers(*args):
    for arg in args:
        print(arg)
