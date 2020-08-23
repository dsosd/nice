import sys

def test_power_of_2(str):
	num = int(str)

	while num % 2 == 0:
		num //= 2

	return "Power of 2:", num == 1

def test_palindrome(str):
	return "Palindromic:", str == str[::-1]

def main():
	#TODO support more options than checking one number
	if len(sys.argv) != 1 + 1:
		print("Incorrect number of arguments")

	num = sys.argv[1]

	tests = [
		test_power_of_2,
		test_palindrome
	]

	[print(*test(num)) for test in tests]

if __name__ == "__main__":
	main()
