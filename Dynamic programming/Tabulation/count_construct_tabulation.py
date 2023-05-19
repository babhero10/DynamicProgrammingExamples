def count_construct(text, list_of_strings):
	text_len = len(text) + 1

	table = [0] * (text_len)

	table[0] = 1

	for i in range(0, text_len):
		if table[i] >= 1:
			for string in list_of_strings:
				if text[i:].find(string) == 0:
					if (i + len(string)) < text_len:
						table[i + len(string)] += table[i]

	return table[text_len - 1]


print(count_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
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