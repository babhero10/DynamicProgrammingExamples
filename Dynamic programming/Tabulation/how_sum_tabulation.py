def how_sum(number, list_of_number):

	table = [None] * (number + 1)
	table[0] = []

	for i in range(0, number + 1):
		if table[i] != None:
			for num in list_of_number:	
				if num + i <= number:
					table[num + i] = table[i] + [num]
						
	return table[number]
	

print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))