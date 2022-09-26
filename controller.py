from user_search import *
from ecspot import *
from logger import *
from importi import *

def hellp():
	num = int(input('Введите "1" Что бы Найти пользователя.\nВведите "2" Что бы Добавить пользователя.\n'))
	if num == 1:
		a = get_list()
		num = search(a)
		recordding(num)

	if num == 2:
		user = user_write()
		log_write(user)