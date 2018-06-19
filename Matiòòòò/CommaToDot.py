#To convert the decimal separator in a file of numbers from a comma to a dot.

x = 1

try:
	while True:

		file_name = 'k%d.txt' % (x)
		file_path = 'data/' + file_name
		file_path_new = 'data/new/' + file_name

		with open(file_path, 'r') as file:
			with open(file_path_new, 'w') as new_file:

				for line in file:
					value_str = line

					for y in range(0, len(value_str)):

						if value_str[y] == ',':
							new_str = '.'
							new_file.write(new_str )
						else:
							new_file.write(value_str[y])
		x += 1
		
except FileNotFoundError:
	print('Non esistono ulteriori files da controllare.\n'
		+ 'Termino l\'esecuzione')

###	_*_ END OF FILE _*_	###