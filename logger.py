from datetime import datetime as dt


def recordding(data):
	time = dt.now().strftime('%H:%M')
	with open('log.csv', 'a', encoding='UTF-8') as file:
		file.write('{};"Поиск: ";{}\n'
						.format(time, data))
def log_write(data):
	time = dt.now().strftime('%H:%M')
	with open('log.csv', 'a', encoding='UTF-8') as file:
		file.write('{};"Добавлен в список: ";{}\n'
						.format(time, data))
	print('Пользователь добавлен')