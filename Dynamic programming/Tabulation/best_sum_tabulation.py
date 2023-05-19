def best_sum(number, list_of_number):

	table = [None] * (number + 1)
	table[0] = []

	for i in range(0, number + 1):
		if table[i] != None:
			for num in list_of_number:

				comb = table[i] + [num]

				if num + i <= number:
					if table[i + num] == None or len(table[i + num]) > len(comb):
						table[num + i] = comb			
						
	return table[number]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))