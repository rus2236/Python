n = int(input('Введите количество билетов: '))
summa = 0
count = 0
for i in range(1, n+1):
    age = int(input('Введите возраст: '))
    if age > 24:
        summa += 1390
        count += 1
    elif 18 <= age <= 24:
        summa += 990
        count += 1
    elif 0 < age < 18:
        summa += 0
        count += 1
if count > 3:
    summa = summa - summa * 0.1
    
print('Сумма к оплате:',summa, 'руб.')
