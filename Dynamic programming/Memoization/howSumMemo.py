def how_sum(number, list_of_numbers):
	return how_sum_helper(number, list_of_numbers, {})

def how_sum_helper(number, list_of_numbers, memo):

	if number in memo:
		return memo[number]

	if number == 0:
		return []

	if number < 0:
		return None

	for sub_value in list_of_numbers:

		sum_value = number - sub_value

		get_list = how_sum_helper(sum_value, list_of_numbers, memo)
		
		if get_list != None:
			get_list.append(sub_value)
			memo[number] = get_list[:]
			return memo[number]

	memo[number] = None
	return None

print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))