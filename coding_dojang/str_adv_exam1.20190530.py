import string
strings = " "+input()
table = str.maketrans(string.punctuation, ' '*32)
strings = strings.translate(table)
cnt_the = strings.count(" the ")
print(cnt_the)
# cnt_the2 = strings.count("the ")
# cnt_the2 = strings.count("the")




# 1.문자열을 받고
# 2.해당 문자열만 숫자를 세서
# 2-1. 문자열 중에서 해당 단독문자열만 제외시켜야하기때문에
# 2-2. 어떻게 여기서 걸러내는지가 중요하다.
# 3.그 개수를 내 보낸다.#

# >>> table = str.maketrans('aeiou', '12345')
# >>> 'apple'.translate(table)
# '1ppl2'