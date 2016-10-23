"""
Given a matrix A and a eigenvector X0,
Find the dominant eigenvalue and eigenvector
"""

#returns 2d list of a square matrix input from console
def input_square_matrix(order=None):

	if(order == None):
		order = int(input("Enter order of square matrix: "))

	print("input each row separated by newline and each item separated by space")

	#initialize blank 2d matrix with one zero element
	input_matrix = [[0]]

	for i in range(order):
		tmp_arr = list( map(float, input().split()) )
		input_matrix.append(tmp_arr)

	#remove init zero element
	input_matrix.pop(0)	

	return input_matrix

#multiplies a given matrix with another single column matrix
def multiply_eigen(given_matrix,eigen_matrix):
	res_matrix = []
	order = len(given_matrix)

	for i in range(order):
		elem = 0
		for j in range(order):
			elem += given_matrix[i][j] * eigen_matrix[0][j]
		res_matrix.append(elem)

	return res_matrix

def transpose_array(arr):
	trans = [[0]]
	for i in range(len(arr)):
		trans.append([arr[i],])
	trans.pop(0)
	return trans

#calculates eigenvalue and eigenmatrix and returns a list
def get_eigens(given_matrix,eigen_matrix):
	multiplied = multiply_eigen(given_matrix,eigen_matrix)

	lam = max(multiplied)
	rounded_multiplied = list(map(lambda x: round(x/lam,3), multiplied))
	
	return [lam,[rounded_multiplied,],]


#main code here
given_matrix = input_square_matrix()
#print(given_matrix)
print("Input eigenmatrix")
eigen_matrix = input_square_matrix(1)
#print(eigen_matrix[0])

iterations = [get_eigens(given_matrix,eigen_matrix),]

found = False
while(found is False):
	new_iter = get_eigens(given_matrix,iterations[-1][1])

	print("iteration " + str(len(iterations)) + ": " + str(new_iter[0]) + " vs " + str(iterations[-1][0]))
	#check if eigenvalue has repeated itself
	if(new_iter[0] == iterations[-1][0]):
		found = True

	iterations.append(new_iter)

print("Dominant Eigenvalue: " + str(iterations[-1][0]))
print("Dominant Eigenvector: " + str(iterations[-1][1][0]) + "^T")
