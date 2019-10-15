# sieve_till_n.py
import pprint

def sieve(n):
	'''
	print all prime integers till n
	input n
	output list of prime integers
	'''
	
	dct_n = {}
	for _ in range(2, n+1):
		dct_n[_] = {
					'is_prime': False,
					'is_marked': False,
					}
	for curr_int in dct_n:
		# print(curr_int)
		# print('-------------')
		for _ in range(curr_int, 11, curr_int):
			dct_n[_]['is_marked'] = True
	pprint.pprint(dct_n)

if __name__ == '__main__':
	sieve(100)