def all_construct(text, list_of_strings):
	return all_construct_helper(text, list_of_strings, {})

def all_construct_helper(text, list_of_strings, memo):

	if text in memo:
		return memo[text]

	if len(text) == 0:
		return [[]]

	result = []

	for string in list_of_strings:

		index = text.find(string)

		if index == 0:
			con = all_construct_helper(text[len(string):], list_of_strings, memo)
			r = list(map(lambda x: [string] + x, con))
			result += r 
			

	memo[text] = result		
	return result

print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(all_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(all_construct("aaaaaaaaaaaaaz", [
									'a',
									'aa',
									'aaa',
									'aaaa',
									'aaaaa',
									]))