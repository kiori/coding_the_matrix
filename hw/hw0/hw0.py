# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [xx for xx in L if xx%num!=0]



## Problem 2
def myLists(L): return [list(range(1, (xx+1))) for xx in L]



## Problem 3
def myFunctionComposition(f, g): return {key:g[value] for key,value in f.items()}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j)
complex_addition_b = 1j
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
	current = 0
	if len(L)!=0:
		for number in L:
			current += number
	return current


## Problem 7
def myProduct(L):
	if len(L)!=0:
		current = 1
		for number in L:
			current *= number
	else:
		current = 0 

	return current



## Problem 8
def myMin(L):
	return sorted(L).pop(0)



## Problem 9
def myConcat(L):
	current = ''
	for word in L:
		if type(word) is str:
			current += word

	return current


## Problem 10
def myUnion(L):
	current = set()
	for item in L:
		current.update(item)
	return current

