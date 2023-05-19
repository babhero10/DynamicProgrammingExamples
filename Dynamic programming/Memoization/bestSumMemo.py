def best_sum(number, list_of_numbers):
	return best_sum_helper(number, list_of_numbers, {})

def best_sum_helper(number, list_of_numbers, memo):

	if number in memo:
		return memo[number]

	if number == 0:
		return []

	if number < 0:
		return None

	short_comb = None

	for sub_value in list_of_numbers:

		sum_value = number - sub_value

		get_list = best_sum_helper(sum_value, list_of_numbers, memo)

		if get_list != None:
			new_list = get_list[:] + [sub_value]

			if short_comb == None or len(new_list) < len(short_comb):
				short_comb = new_list
				

	memo[number] = short_comb
	
	return memo[number]

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))