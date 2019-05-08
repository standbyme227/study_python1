## 동물은 object의 일종(is-a)이다 (네, 조금 헷갈리죠) 추가 점수 문제가 있습니다.
class 동물(object):
    pass


## is-a
class 개(동물):
    def __init__(self, 이름):
        ## ??
        self.이름 = 이름


## is-a
class 고양이(동물):
    def __init__(self, 이름):
        ## ??
        self.이름 = 이름


## has-a
class 사람(object):
    def __init__(self, 이름):
        ## ??
        self.이름 = 이름

        ## 사람은 어떤 종류의 애완동물을 갖고 있다.
        self.애완동물 = None


## has-a
class 노동자(사람):
    def __init__(self, 이름, 월급):
        ## ?? 음 이 외계어는 뭐죠?
        super(노동자, self).__init__(이름)
        self.월급 = 월급


# ??
class 물고기(object):
    pass


# is-a
class 연어(물고기):
    pass


## is-a
class 대서양연어(물고기):
    pass


## 나그네는 개의 일종(is-a) 이다
나그네 = 개("나그네")

## is_a
악마 = 고양이("악마")

## is_a
영희 = 사람("영희")

## has_a
영희.애완동물 = 악마

## is_a
철수 = 노동자("철수", 120000)

## has_a
철수.애완동물 = 나그네

## is_a
팔딱이 = 물고기()

## is_a
동구 = 연어()

## is-a
하루 = 대서양연어()
