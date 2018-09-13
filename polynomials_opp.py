# polynomials_opp.py

def addpoly(p1,p2):
	o_dict = {}
	o_lst = []
	
	for term in p1:
		if term[1] not in o_dict:
			o_dict[term[1]] = 0
		o_dict[term[1]] += term[0]
	for term in p2:
		if term[1] not in o_dict:
			o_dict[term[1]] = 0
		o_dict[term[1]] += term[0]
		if term[0] == 0:
			del o_dict[term[1]]
	max_key = 0
	for _ in o_dict:
		if _ > max_key:
			max_key = _
	for _ in range(max_key + 1, 0 , -1):
		if _ in o_dict:
			o_lst.append((o_dict[_], _))

	return o_lst

	
def multpoly(p1,p2):
	sum_lst = []
	
	for term in p1:
		tmp_lst = []
		for term1 in p2:
			coeff = term[0] * term1[0]
			expon = term[1] + term1[1]
			tmp_lst.append((coeff, expon))
			# print('tmp_lst')
			# print(tmp_lst)
		print('tmp_lst')
		print(tmp_lst)
		print('sum_lst')
		print(sum_lst)
		sum_lst = addpoly(sum_lst, tmp_lst)

		
	return sum_lst


if __name__ == '__main__':
	# print(addpoly(
	# 	[(4, 9), (3, 5)],
	# 	[(4, 11), (2, 5)],
	# 	))
	# print(addpoly([(4,3),(3,0)],[(-4,3),(2,1)]))
	# print(multpoly([(4,3),(3,0)],[(-4,3),(2,1)]))
	# print(multpoly(
	# 	[(4, 9), (3, 5)],
	# 	[(4, 11), (2, 5)],
	# 	))
	print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))