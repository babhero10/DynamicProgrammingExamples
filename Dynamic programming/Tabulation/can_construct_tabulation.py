def can_construct(text, list_of_strings):
	text_len = len(text) + 1

	table = [False] * (text_len)

	table[0] = True

	for i in range(0, text_len):
		if table[i] == True:
			for string in list_of_strings:
				if text[i:].find(string) == 0:
					if (i + len(string)) < text_len:
						table[i + len(string)] = True

	return table[text_len - 1]


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