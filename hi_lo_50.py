import random


max_50, iter_50 = 0, 0
max_60, iter_60 = 0, 0
max_70, iter_70 = 0, 0
max_80, iter_80 = 0, 0
max_90, iter_90 = 0, 0

for i in range(1000000):  # Количество ставок
    bet = random.randint(0, 100)
    #print(bet)
    if bet > 50:
        iter_50 = 0
    else:
        iter_50 += 1
        if max_50 < iter_50:
            max_50 = iter_50

    if bet > 60:
        iter_60 = 0
    else:
        iter_60 += 1
        if max_60 < iter_60:
            max_60 = iter_60

    if bet > 70:
        iter_70 = 0
    else:
        iter_70 += 1
        if max_70 < iter_70:
            max_70 = iter_70

    if bet > 80:
        iter_80 = 0
    else:
        iter_80 += 1
        if max_80 < iter_80:
            max_80 = iter_80

    if bet > 90:
        iter_90 = 0
    else:
        iter_90 += 1
        if max_90 < iter_90:
            max_90 = iter_90

print('max_50 =', max_50)
print('max_60 =', max_60)
print('max_70 =', max_70)
print('max_80 =', max_80)
print('max_90 =', max_90)
