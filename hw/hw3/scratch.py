import numpy as np

#Problem 6 Matrix-Matrix Multiplication

#Number 1
A = np.matrix([[2,3],[4,2]])
B = np.matrix([[1,2],[2,3]])
print "Problem 1: "
print A*B
print "\n"

#Number 2
A = np.matrix([[2,4,1],[3,0,-1]])
B = np.matrix([[1,2,0],[5,1,1],[2,3,0]])
print "Problem 2: "
print A*B
print "\n"


#Number 3
A = np.matrix([[2,2,1]])
B = np.matrix([[3,1],[-2,6],[1,-1]])
print "Problem 3: "
print A*B
print "\n"


#Number 4
A = np.matrix([[1,2,3]])
B = np.matrix([[1],[2],[3]])
print "Problem 4: "
print A*B
print "\n"


#Number 5
A = np.matrix([[1],[2],[3]])
B = np.matrix([[1,2,3]])
print "Problem 5: "
print A*B
print "\n"


#Number 6
A = np.transpose(np.matrix([[4,1,-3],[2,2,-2]]))
B = np.matrix([[-1,1],[1,0]])
print "Problem 6: "
print A*B
print "\n"

#Problem 7
A = np.matrix([[2,0,1,5],[1,-4,6,2],[3,0,-4,2],[3,4,0,-2]])
B1 = np.matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
B2 = np.matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
B3 = np.matrix([[0,0,0,1],[0,1,0,0],[1,0,0,0],[0,0,1,0]])

list_of_Bs = [B1,B2,B3]

for mat in list_of_Bs:
	print "A*B:" 
	print A*mat
	print "\n"
	print mat*A
	print "\n"

#Problem 8
A = np.matrix([[1,2], [0,1]])
B = np.matrix([[1,3],[0,1]])
A*B

A = np.matrix([[1,1], [0,1]])
print A*A
print A**3

#Problem 9
A = np.matrix([[4,2,1,-1],[1,5,-2,3],[4,4,4,0],[-1,6,2,-5]])
B1 = np.matrix([[0,0,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]])
B2 = np.matrix([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0]])
B3 = np.matrix([[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]])
B4 = np.matrix([[0,1,0,1],[0,0,0,0],[0,0,0,0],[0,1,0,0]])
B5 = np.matrix([[0,0,0,2],[0,0,0,0],[0,0,0,0],[0,-3,0,0]])
B6 = np.matrix([[-1,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,3]])

for mat in [B1,B2,B3,B4,B5,B6]:
	print "A*B:" 
	print (A*mat).tolist()
	print (mat*A).tolist()
	print "\n"

#Problem 10
#  PartA
M = listlist2mat([[2,3,1],[1,3,4]])
V = list2vec([2,2,3])
matrix_vector_mul(M,V)

#  PartB
V = list2vec([2,4,1])
M = listlist2mat([[1,2,0],[5,1,1],[2,3,0]])
vector_matrix_mul(V,M)

#  PartC
V = list2vec([2,1])
M = listlist2mat([[3,1,5,2],[-2,6,1,-1]])
print vector_matrix_mul(V,M)

#  PartD
M = listlist2mat([[1,2,3,4],[1,1,3,1]])
V = list2vec([1,2,3,4])
matrix_vector_mul(M,V)

#  PartE
V = np.transpose(np.matrix([[4],[1],[-3]]))
M = np.matrix([[-1,1,1],[1,0,2],[0,1,-1]])

V1 = list2vec([4,1,3])
M1 = listlist2mat([[-1,1,1], [1,0,2],[0,1,-1]])
# vector_matrix_mul(V,M)

def lin_comb_mat_vec_mult(M,v):
    assert(M.D[1] == v.D)
    import vec, matutil
    comb=sum(v[i]*matutil.mat2coldict(M)[i] for i in v.D)
    return comb

def lin_comb_vec_mat_mult(v, M):
    assert(v.D == M.D[0])
    import vec, matutil
    comb=sum(v[i]*matutil.mat2rowdict(M)[i] for i in v.D)
    return comb

def dot_product_mat_vec_mult(M, v):
    assert(M.D[1] == v.D)
    import vec, matutil
    vv = {i:vec.dot(matutil.mat2rowdict(M)[i], v) for i in M.D[0]}
    return vec.Vec(M.D[0], vv)

def Mv_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    import vec, matutil
    B_dict = matutil.mat2coldict(B)
    print B_dict
    return B_dict


def dot_prod_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    import vec, matutil
    A_dict = matutil.mat2rowdict(A)
    B_dict = matutil.mat2coldict(B)
    dp = {(i,j): A_dict[i]*B_dict[j] for j in B_dict.keys() for i in A_dict.keys()}
    return Mat((set(A_dict.keys()), set(B_dict.keys())), dp)

#Problem 18
#part 1,2
A = np.array([[3,4],[2,1]])
B = np.array([[1],[0]])
np.linalg.solve(A,B)

#part 3,4
A = np.array([[3,4],[2,1]])
B = np.array([[0],[1]])
np.linalg.solve(A,B)

#Problem 19

#1
A=np.matrix([[5,1],[9,2]])
B=np.matrix([[2,-1],[-9,5]])
print A*B
print B*A
print '\n'

#2
A=np.matrix([[2,0],[0,1]])
B=np.matrix([[0.5,0],[0,1]])
print A*B
print B*A
print '\n'

#3
A=np.matrix([[3,1],[0,2]])
B=np.matrix([[1,1.0/6],[-2,0.5]])
print A*B
print B*A
print '\n'

#3
A=np.matrix([[1,0,1],[0,1,0]])
B=np.matrix([[0,1],[0,1],[1,1]])
print A*B
print B*A
print '\n'
