def fib(number):
	return fib_helper(number, {})

def fib_helper(number, memo):

	if number in memo:
		return memo[number]

	if number <= 2:
		return 1

	memo[number] = fib_helper(number - 1, memo) + fib_helper(number - 2, memo)
	return memo[number]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))