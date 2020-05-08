import random


min_depo = 100000.0
for _ in range(1000):
    if min_depo < 0:
        break
    start_depo = 100000.0  # Старт Депо
    stop_depo = start_depo + start_depo * 0.00003  # Стоп Депо
    bet_percent = 0.00001  # Процент ставки от депо
    bet = start_depo * bet_percent  # Первоначальная ставка
    step_percent = 0.25
    # print(start_depo)
    # print(bet)
    # print(stop_depo)
    depo = start_depo
    plus = 0
    minus = 0
    while True:
        if min_depo > depo:
            min_depo = depo
        if stop_depo < depo or depo < 0.0:
            break
        bet_iter = random.randint(0, 99)
        if bet_iter > 50:
            depo = depo + bet
            bet = bet - bet * step_percent
            plus += 1
        else:
            depo = depo - bet
            bet = bet + bet * step_percent
            minus += 1

    print(plus)
    print(minus)
    print(depo)
print(min_depo)