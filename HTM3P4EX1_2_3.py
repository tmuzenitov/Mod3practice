import json

register = {'testlog': 'testpasswd'}
with open('register.json', 'w') as f:
	json.dump(register, f)

def add_register(login, passwd):
	with open('register.json', 'r') as f:
		register = json.load(f)
	if login not in register.keys():
		register[login] = passwd
		with open('register.json', 'w') as f:
			json.dump(register, f)
			print('Успешная регистрация')
	else:
		print('Пользователь с таким логином уже существует')

def in_register():
	with open('register.json', 'r') as f:
		register = json.load(f)
		login = input('Введите логин: ')
		passwd = input('Введите пароль: ')
	if login in register.keys():
		print('Успешный вход!')
	else:
		print('Такого пользователя не существует')

while True:
	q1 = input('Вход или регистрация?')
	if q1 == 'регистрация':
		add_register(input('Введите новый логин: '), input('Введите новый пароль: '))
		break
	elif q1 == 'вход':
		print(in_register())
		break