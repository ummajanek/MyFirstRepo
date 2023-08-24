money =int(input("Введите сумму вклада  "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
values=list(map(float,per_cent.values()))
for i in values :
      i=int(i*money/100)
      deposit.append(i)
print('deposit=',deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))


