# Задача 4. Имеется 1000 рублей. Бык стоит – 100
# рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все
# эти деньги, если всего надо купить 100 голов
# скота?

money = 1000

b_count = 0
k_count = 0
t_count = 0

b_price = 100
k_price = 50
t_price = 5

b_count = money // b_price
k_count = money // k_price
t_count = money // t_price

for b in range(b_count+1):
    for k in range(k_count+1):
        for t in range(t_count):
            if b+k+t==100 and b*b_price + k*k_price + t*t_price==1000:
                print(f'{b}, {k}, {t}')
            
