import math
import sys

def test_power_of_2(str):
	num = int(str)

	while num % 2 == 0:
		num //= 2

	return "Power of 2:", num == 1

def test_palindrome(str):
	return "Palindromic:", str == str[::-1]

def test_square(str):
	num = int(str)

	return "Square number:", math.isqrt(num)**2 == num

def main():
	#TODO support more options than checking one number
	if len(sys.argv) != 1 + 1:
		print("Incorrect number of arguments")

	num = sys.argv[1]

	tests = [
		test_power_of_2,
		test_palindrome,
		test_square
	]

	[print(*test(num)) for test in tests]

if __name__ == "__main__":
	main()
