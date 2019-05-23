a = list(map(int, input().split()))
total_point = 0
for point in a:
    if point >= 0 and point <= 100:
        total_point += point
    else:
        print("잘못된 점수")
        exit()
if total_point / 4 >= 80:
    print("합격")
else:
    print("불합격")