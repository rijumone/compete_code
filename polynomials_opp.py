# polynomials_opp.py

def addpoly(p1,p2):
	o_dict = {}
	p_dict = {}
	o_lst = []
	for term in p1:
		if term[1] not in o_dict:
			o_dict[term[1]] = 0
		o_dict[term[1]] += term[0]
	for term in p2:
		if term[1] not in o_dict:
			o_dict[term[1]] = 0
		o_dict[term[1]] += term[0]
		if o_dict[term[1]] == 0:
			del o_dict[term[1]]
	max_key = 0
	for _ in o_dict:
		if _ > max_key:
			max_key = _
	for _ in range(max_key + 1, 0 , -1):
		if _ in o_dict:
			p_dict[_] = o_dict[_]
			o_lst.append((p_dict[_], _))

	return o_lst

	
def multpoly(p1,p2):
	pass

if __name__ == '__main__':
	print(addpoly(
		[(4, 9), (3, 5)],
		[(4, 11), (2, 5)],
		))

