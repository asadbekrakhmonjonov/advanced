from datetime import date
class LotteryDraw:
    def __init__(self,round_week: int,round_date: date,numbers: list):
        self.round_week = round_week
        self.round_date = round_date
        self.numbers = numbers
round1 = LotteryDraw(1,date(2024,1,13),[1,2,3,4,5,6,7,8])
print(round1.round_week)
print(round1.round_date)
for i in round1.numbers:
    print(i)
