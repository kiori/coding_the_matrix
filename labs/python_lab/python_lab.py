## Task 1
minutes_in_week = 60*24*7

## Task 2
remainder_without_mod = 2304811-47*(2304811//47)

## Task 3
divisible_by_3 = ((673+909)% 3 == 0)

## Task 4
x = -9
y = 1/2
statement_val = 1.0

## Task 5
first_five_squares = { xx*xx for xx in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**xx for xx in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 1, 2, 3 }
Y1 = { 5, 7, 11 }

## Task 8: enter in the two new sets
X2 = { 1, 2, 4 }
Y2 = { 8, 16, 32 }

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {xx*base**2+yy*base**1+zz*base**0 for xx in digits for yy in digits for zz in digits}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = {xx for xx in S if xx in T}

## Task 11
L_average = sum([20, 10, 15, 75])/len([20, 10, 15, 75])

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(ll) for ll in LofL])

## Task 13
cartesian_product = [ [x,y] for x in {'A','B','C'} for y in {1,2,3} ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if sum((i,k,j))==0]

## Task 15
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if (sum([i,k,j])==0 and (i!=0 or j!=0 or k!=0))]

## Task 16
first_of_tuples_list = [(i,j,k) for i in S for j in S for k in S if (sum([i,k,j])==0 and (i!=0 or j!=0 or k!=0))][0]

## Task 17
L1 = [1,1,2,3,4] # <-- want len(L1) != len(list(set(L1)))
L2 = ['1',2,3,4,1] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {xx for xx in range(1,100,2)}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))

## Task 20
list_sum_zip = [x+y for x,y in zip([10,25,40],[1, 15, 20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [dlist[xx][k] for xx in range(len(dlist))]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [xx[k] if (k in xx) else ('NOT PRESENT') for xx in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [xx[k] if (k in xx) else ('NOT PRESENT') for xx in dlist] # <-- as you do here

## Task 23
square_dict = {xx: xx*xx for xx in range(0,100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {xx:xx for xx in D}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {sum([i*base**2, j*base**1, k*base**0]): [i, j, k] for i in digits for j in digits for k in digits}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = {names[k]:v for k,v in d.items()}

## Task 27
def nextInts(L): return [xx+1 for xx in L]

## Task 28
def cubes(L): return [xx**3 for xx in L] 

## Task 29
def dict2list(dct, keylist): return [ dct[key] for key in keylist]

## Task 30 
def list2dict(L, keylist): return { key:value for key,value in zip(keylist,L)} 

