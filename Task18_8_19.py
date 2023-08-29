number_of_tickets=int(input("Введите количество билетов  "))
sum_zakaz=0
i=1
while i<= number_of_tickets:
    try:
      age=int(input("Введите возраст участника  "))
      if age > 100 or age <= 0:
        raise ValueError('Указан недопустимый возраст участника')
    except ValueError as error:
        print(error)
        print ("Повторите ввод")
    else:
      i+=1
      if age < 18:
          continue
      elif 18<=age<25:
          sum_zakaz+=990
      else: sum_zakaz+=1390
if number_of_tickets >3:
      sum_zakaz=sum_zakaz-0.1*sum_zakaz
print (f"Полная стоимость заказа - {sum_zakaz} руб.")
