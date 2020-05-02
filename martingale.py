import random

depo = 10000
profit = 0
max_bet = 0
min_profit = 0
#max_iter = 0
for i in range(10000):
    if profit >= 0:
        bet = 1
        profit = 0
        #max_iter = 1
    else:
        bet = bet * 2
    if bet > max_bet:
        max_bet = bet
    bet_int = random.randint(0, 1)
    fallout_int = random.randint(0, 1)
    if bet_int == fallout_int:
        depo = depo + bet
        profit = profit + bet
    else:
        depo = depo - bet
        profit = profit - bet

    if profit < min_profit:
        min_profit = profit
    print('bet =', bet)
    print('profit =', profit)
print(depo)
print('max_bet =', max_bet)
print('min_profit =', min_profit)