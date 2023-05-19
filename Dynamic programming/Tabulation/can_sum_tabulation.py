def can_sum(number, list_of_number):

	table = [False] * (number + 1)
	table[0] = True

	for i in range(0, number + 1):
		if table[i]:
			for num in list_of_number:
				if num + i <= number:
					table[num + i] = True

	return table[number]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))