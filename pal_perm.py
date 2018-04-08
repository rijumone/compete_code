"""
return count of possible palindromes of a given string
does NOT account for duplicate letters
"""
import math

def chkPalindromePossible(string):
	"""
	check whether str can be converted to
	a palidrome or not
	"""
	unmatched = 0
	for letter in string:
		if string.count(letter) < 2:
			unmatched += 1
	if len(string) % 2 == 1:
		if unmatched < 2:
			return True
	else:
		if unmatched < 1:
			return True
	return False

def math_factorial(integer):
	if integer == 1:
		return 1
	else:
		return integer * math_factorial(integer-1)

check_this_str = input()
if chkPalindromePossible(check_this_str):
	print(math_factorial(math.floor(len(check_this_str)/2)))
else:
	print(0)


"""
algorithm count_palindrome_str(str)
INPUT string str
function chkPalindromePossible(string):
	Let unmatched <- 0
	for j<-0 to string.length-1
		if string.count(string[j]) < 2 then
			unmatched += 1
	if string.length % 2 == 1 then
		if unmatched < 2 then
			return True
	else
		if unmatched < 1 then
			return True
	return False

function math_factorial(integer)
	if integer == 1 then
		return 1
	else
		return integer * math_factorial(integer-1)


if chkPalindromePossible(str):
	return math_factorial(math.floor(len(str)/2))
else:
	return 0

"""