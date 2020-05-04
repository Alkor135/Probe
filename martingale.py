import random

depo = 100000
profit = 0
max_bet = 0
min_profit = 0
iter = 0
max_iter = 0
for i in range(1000000):  # Количество ставок
    if profit >= 0:  # Если профит от предыдущей сделки положительный
        bet = 1  # Ставку устанавливаем в 1
        profit = 0  # Профит обнуляем
        iter = 0  # Обнуляем количество ставок
    else:  # Если профит от предыдущей сделки отрицательный
        iter += 1  # Увеличиваем счетчик иттераций на 1 для подсчета колен
        bet = bet * 2  # Увеличиваем ставку в 2 раза
        if max_iter < iter:  # Если максимальное количество иттераций меньше чем текущее кол-во иттераций
            max_iter = iter  # Записываем новое количество иттераций, для подсчета макс кол-ва колен
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
    #print('bet =', bet)
    #print('profit =', profit)
    #print(max_iter)
print(depo)
print('max_bet =', max_bet)
print('min_profit =', min_profit)
print('max_iter =', max_iter)