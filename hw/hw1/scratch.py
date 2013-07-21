from GF2 import one
import numpy as np
from itertools import chain, combinations

def problems_4_and_5(problem):

	u_answer = np.array([0, 0 , one, 0, 0, one,0 ])
	v_answer = np.array([0, one , 0, 0, 0, one , 0])

	if problem==4:
		dict_str = {'a':'1100000','b':'0110000','c':'0011000','d':'0001100','e':'0000110','f':'0000011'}
	if problem==5:
	dict_str = {'a':'1110000','b':'0111000','c':'0011100','d':'0001110','e':'0000111','f':'0000011'}

	def change_dict(value):
		new_value = []
		for char in value:
			if char=='1':
				new_value.append(one)
			else:
				new_value.append(0)
		return np.array(new_value)

	dict_array = {key:change_dict(value) for key, value in dict_str.iteritems()}
	key_list = dict_array.keys()

	combs = []
	for i in xrange(2, len(key_list)+1):
	    els = [list(x) for x in combinations(key_list, i)]
	    combs.append(els)

	flat_combs = [val for subl in combs for val in subl]

	for index, vectors in enumerate(flat_combs):
		vector_sum=dict_array[vectors[0]]
		for vector in vectors[1:]:
			vector_sum = vector_sum + dict_array[vector]
		print index, " end: ", vector_sum	
		if (vector_sum==u_answer).all():
			print "U-Answer Vector: ", sorted(vectors)
		if (vector_sum==v_answer).all():
			print "V-Answer Vector: ", sorted(vectors)