x = int(input('Сумма вклада: '))
p = int(input('Процентная ставка: '))
y = int(input('Желаемая сумма на вкладе: '))
i = 0
while x < y:
	x *= 1 + p / 100
	x = int(100 * x) / 100
	i += 1
print(i)