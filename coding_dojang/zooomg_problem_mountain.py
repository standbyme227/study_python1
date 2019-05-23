# a = list(int(input()))


# 1 이면 2되고 1이면 3이되고
# 1213121

# 일정한 패턴이 반복됨으로 재귀로 처리해야하는게 맞는듯 하다.

# 어떻게 해야할까?
# 일단 가장 높은 수가 들어온다.
# 일단 가장 높은 수가 중앙에 있고
# 양쪽에 -1이 된 값이 온다.
# 또 그 세개가 들어가서 똑같은 걸 반복한다.
# 그럼 들어가는 건 리스트다.

# def moutain(a_list):
#     for i in a_list:
#         if len(a_list) == 1:
#             a_list = [i - 1] + [i] + [i - 1]
#         elif i < max(a_list):
#             i = [i - 1] + [i] + [i - 1]


# def add_blank(a_list):
#     a_list.insert(0, '')
#     a_list.append('')
#     return a_list


max_h = int(input())
a_list = []
for i in range(max_h, 0, -1):
    str_i = str(i)
    str_i = str_i.center(len(str_i) + 2)
    if i == max_h:
        a_list.append(str_i)
        a_str = " ".join(a_list)
    else:
        a_str = str_i.join(a_list)
    a_list = a_str.split(" ")
print(''.join(a_list))
