# 문자열 바꾸기
"hello world!!".replace("hello", "fuck")


# 문자 바꾸기
# 1. table 지정 -> str.maketrans("지정문자", "바꿀문자")
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)


# 문자열 분리하기
# 문자열.split(기준 문자열)
str_list = "apple pear grape pineapple orange".split()


# 구분자 문자열과 문자열 리스트 연결하기
" ".join(str_list)


# 대소문자
b = "python".upper()
b.lower()


# 공백삭제 or 특정문자삭제
# strip 메서드 종류 안에 문자열의 args를 넣으면 된다.
"ㄴㅇㄹㄴㅇㄹㄴㅇㄹ".lstrip()
"sdsfsdfds".rstrip()
"sdfsdfdsf".strip()


# 문자열 정렬
'sdfsdfsd'.ljust()
'ghghfh'.rjust()
'dssfsdf'.center()


# 문자열 위치 찾기
# find는 찾는 문자열이 없으면 -1을 반환
'sdfdsfdssdfs'.find('df')
'ㄴㅇㄹㅇㄴㄹㄴㅇㄴㅇㄹㄴ'.rfind('ㄴㅇ') # 오른쪽부터
# index는 찾는 문자열이 없으면 error
'sdfdsffsdsdf'.index('df')
'sdfdsfsdfsdf'.rindex('sdf') #오른쪽부터


#문자열 개수 세기
#특정문자열의 개수를 세서 반환함.
'sdfdsfdsfrffgs'.count('sdf')

