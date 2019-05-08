from sys import exit
from random import randint
from textwrap import dedent


# TODO 장면을 구현.
# 사실 뭘해야하는지도 잘 모르겠었다.


class 장면(object):
    def 입장(self):
        print("아직 만들지 않은 장면입니다.")
        print("상속해 입장()을 구현하세요.")
        exit(1)


class 엔진(object):
    def __init__(self, 장면_지도):
        self.장면_지도 = 장면_지도

    def 플레이(self):
        현재_장면 = self.장면_지도.서막_장면()
        마지막_장면 = self.장면_지도.다음_장면("끝")

        while 현재_장면 != 마지막_장면:
            마지막_장면_이름 = 현재_장면.입장()
            현재_장면 = self.장면_지도.다음_장면(마지막_장면_이름)

        # 마지막 장면을 출력하도록 한다.
        현재_장면.입장()


class 사망(장면):
    입담등 = [
        
    ]
    def 입장(self):
        return ""


class 중앙_복도(장면):
    def 입장(self):
        pass


class 레이져_무기고(장면):
    def 입장(self):
        pass


class 함교(장면):
    def 입장(self):
        pass


class 구명정(장면):
    def 입장(self):
        pass


class 지도(object):
    def __init__(self, 시작_장면):
        pass

    def 다음_장면(self, 장면_이름):
        pass

    def 서막_장면(self):
        pass


게임_지도 = 지도("중앙_복도")
게임_엔진 = 엔진(게임_지도)
게임_엔진.플레이()
