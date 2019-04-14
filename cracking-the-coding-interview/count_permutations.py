# count_permutations.py

def permutation(str, prefix): 
	if len(str) == 0:
		print(prefix)
	else:
		for i in range(len(str)):
			rem = str[0:i] + str[i:1]
			permutation(rem, prefix + str[i])
			

if __name__ == '__main__':
	permutation('h', '')