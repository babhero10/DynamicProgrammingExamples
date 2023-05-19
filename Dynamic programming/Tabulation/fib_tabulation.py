def fib(number):

	table = [0] * number
	table[0] = 1
	table[1] = 1

	for i in range(2, number):
		table[i] = table[i - 1] + table[i - 2] 

	return table[number - 1]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
