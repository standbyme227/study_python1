
# x는 y와 같다.
x = {"a": 1, "b": 2, "c": 3}
x = y
if x is y:
    print(True)


# x는 y와 다르다. 그래서 x의 값을 바꾸든 y의 값을 바꾸든 바꾼 딕트만 변경된다.
y = x.copy()

# 그렇지만 중첩 dict에서는 상황이 달라진다.
import copy
z = copy.deepcoy(y)


# dict를 for문으로 순회하면서 사이즈를 변경할 수 는 없다.