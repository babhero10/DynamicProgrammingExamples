def all_construct(text, list_of_strings):
	text_len = len(text) + 1

	table = [[] for i in range(0, text_len)]

	table[0] = [[]]

	for i in range(0, text_len):
		for string in list_of_strings:
			if text[i:].find(string) == 0:
				if (i + len(string)) < text_len and len(table[i]) >= 1:
					combination = list(map(lambda x: x + [string] , table[i]))
					table[i + len(string)] += combination[:]

	return table[text_len - 1]


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