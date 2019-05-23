age = int(input())
balance = 9000

if age >= 7 and age <= 12:
    balance -= 650
elif age >= 13 and age <= 18:
    balance -= 1050
else:
    balance -= 1250
# print(balance)

# x = int(input())
#
# if x > 10 and x <= 20:
#     print("11~20")
# elif x > 20 and x <= 30:
#     print("21~30")
# else:
#     print("아무것도 해당하지 않음")
