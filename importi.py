def user_write():
	with open(f'info.txt', 'a', encoding='UTF-8') as f:
		keys = ['Name', 'Номер', 'Должность', 'ЗП']
		lst= []
		for i in keys:
			lst.append(input(f'Введите {i}: '))
		f.write('\n')
		f.write(', '.join(lst))
	return lst