# 숫자 두개를 받음
# 그 사이를 나열하는 리스트 생성
# 2의 거듭제곱 구성
# 리스트에 저장


a, b = map(int, input().split())
result_list = [2 ** i for i in range(a, b + 1)]
result_list.pop(1)
result_list.pop(-2)
print(result_list)
