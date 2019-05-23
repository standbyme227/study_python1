# 가로 세로 입력
col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '.':
            num_of_mine = 0
            mines = [[num_of_mine + 1 for j in range(j - 1, j + 1) if matrix[-i][j] == "*"] for i in
                     range(i - 1, i + 1)]
print(mines)

# 하나의 포인트를 기점으로 주변에 지뢰를 센다
# 지뢰를 나타낸다.
# 8방위를 다 커버할 수 있도록 처리하고
# 끝자리에 있을때는 다르게 처리되도록 조건을 건다.
# . 을 숫자로 바꾼다.

# 지뢰를 찾는다.
# 지뢰를 센다.
# 모든 곳을 for문으로 돈다.
