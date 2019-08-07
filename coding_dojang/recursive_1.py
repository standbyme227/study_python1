# def factorial(num):
#     if num > 1:
#         return num * factorial(num - 1)
#     else:
#         return num
#
#
#
# def function(입력):
#     if 입력 > 일정값:
#         return function(입력-1) # 입력보다 작은 값
#     else:
#         return 일정값 # 재귀호출 종료
#
#
# def function(입력):
#     if 입력 <= 일정값:
#         return 결과값
#     function(입력보다 작은 값)
#     return 결과값
#
#
# #내가 작성
# def factorial(num):
#     if num <= 1:
#         return num
#     return factorial(num-1)


def factorial_2(num):
    if num <= 1:
        return num
    return num * factorial_2(num-1)

for num in range(10):
    print(factorial_2(num))