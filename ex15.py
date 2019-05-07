from sys import argv

# argv로 unpacking된 arg를 변수에 집어넣음
스크립트, 파일_이름 = argv
# 인코딩_기준 변수에 urf-8이라는 값을 넣어둠
인코딩_기준 = "utf-8"

# 텍스트 변수에는 open 함수로 파일_이름과 동일한 파일을 염
텍스트 = open(파일_이름, encoding=인코딩_기준)

# 출력
print(f"파일 {파일_이름}의 내용:")
# 텍스트에 집어넣은 파일내용을 print하기위해서 read한다음 print
print(텍스트.read())
텍스트.close()

# # 출력
# print("파일이름을 다시 입력해 주세요.")
# # 똑같이 파일이름을 다시 입력.
# 파일_한번더 = input("> ")
#
# 텍스트_한번더 = open(파일_한번더, encoding=인코딩_기준)
#
# print(텍스트_한번더.read())