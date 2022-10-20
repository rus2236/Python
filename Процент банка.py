money = int(input('Введите сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

for key in per_cent:        
    a = round(per_cent[key]* money * 0.1, 2)
    deposit.append(a)
print('Накопленные средства за год:', deposit)

print('Максимальная сумма, которую вы можете заработать — ', max(deposit))
