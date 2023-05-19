def can_construct(text, list_of_strings):
	return can_construct_helper(text, list_of_strings, {})

def can_construct_helper(text, list_of_strings, memo):

	if text in memo:
		return memo[text]

	if len(text) == 0:
		return True

	for string in list_of_strings:

		index = text.find(string)

		if index == 0:
			if can_construct_helper(text[len(string):], list_of_strings, memo):
				memo[text] = True
				return True
	
	memo[text] = False		
	return False

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
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