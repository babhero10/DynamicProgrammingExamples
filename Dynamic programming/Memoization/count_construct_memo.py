def count_construct(text, list_of_strings):
	return count_construct_helper(text, list_of_strings, {})

def count_construct_helper(text, list_of_strings, memo):

	if text in memo:
		return memo[text]

	if len(text) == 0:
		return 1

	totle_con = 0

	for string in list_of_strings:

		index = text.find(string)

		if index == 0:
			totle_con += count_construct_helper(text[len(string):], list_of_strings, memo)
	
	memo[text] = totle_con		
	return totle_con

print(count_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
																'e',
																'ee',
																'eee',
																'eeee',
																'eeeee',
																'eeeeee',
																'eeeeeee',
																'eeeeeeee',
																'eeeeeeeee'
																]))