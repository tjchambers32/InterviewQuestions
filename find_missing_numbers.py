#! python3

import random
import math
import numpy
from sympy.solvers import solve_poly_system
from sympy import symbols

def find_1_missing(n, number_array):
	expected_sum = n*(n+1)/2
	actual_sum = 0
	for num in number_array:
		actual_sum += num
	
	missing_number = expected_sum - actual_sum
	return missing_number

def find_2_missing(n, number_array):
	expected_sum = n*(n+1)/2
	expected_squared_sum = n*(n+1)*(2*n + 1)/6
	# for i in range(1,n+1):
	#     expected_squared_sum += (i**2)
	actual_sum = 0
	actual_squared_sum = 0
	for num in number_array:
		actual_sum += num
		actual_squared_sum += num**2
	
	# squared_number_array = square(number_array)
	
	# Now set up a system of equations and solve
	# k1 + k2 = x                                    -eq. 1
	# k1**2 + k2**2 = y                      -eq. 2

	x = expected_sum - actual_sum
	y = expected_squared_sum - actual_squared_sum

	return solve_quadratic_equation(1, (x * -1), ((x**2)-y)/2 )

def find_3_missing(n, number_array):
	expected_sum = n*(n+1)/2
	expected_squared_sum = n*(n+1)*(2*n+1)/6
	expected_cubed_sum = (n*(n+1)/2)**2
	
	actual_sum = 0
	actual_squared_sum = 0
	actual_cubed_sum = 0
	for num in number_array:
		actual_sum += num
		actual_squared_sum += num**2
		actual_cubed_sum += num**3
		
	x = expected_sum - actual_sum
	y = expected_squared_sum - actual_squared_sum
	z = expected_cubed_sum - actual_cubed_sum
	
	k1, k2, k3 = symbols('k1 k2 k3')
	
	eqs = [k1 + k2 + k3 - x, k1**2 + k2**2 + k3**2 - y, k1**3 + k2**3 + k3**3 - z]
	
	solutions = solve_poly_system(eqs, [k1,k2,k3])
	return solutions[0]

def find_k_missing(n, number_array, k):
	
	expected_kth_sums_list = [0] * k
	expected_kth_sums = numpy.array(expected_kth_sums_list, dtype='int64')
	full_number_array = list(xrange(1,n+1))
	numpy_number_array = numpy.array(full_number_array, dtype='int64')

	actual_kth_sums = [0] * k
	
	for m in range(1, k+1):
		kth_array = numpy.power(numpy_number_array, m)
		expected_kth_sums[m-1] = sum(kth_array)
	
	for num in number_array:
		for index in range(1, k+1):
			actual_kth_sums[index-1] += num**index
	
	# for k missing numbers, i'll need k equations
	equation_variables = symbols('k0:%d'%(k))
	equations = {}
	
	for j in range(1, k+1):
		equation_name = ""
		for h in range(1, k+1):
			if (h != k):
				equation_name += str(equation_variables[h-1]) + "**" + str(j) + " + "
			else:
				equation_name += str(equation_variables[h-1]) + "**" + str(j)
		equations[j-1] = equation_name
		
	equation_list = list()
	listIndex = 0
	for key, value in equations.iteritems():
		listIndex += 1
		equation_list.append(value + " - " + str((expected_kth_sums[listIndex-1] - actual_kth_sums[listIndex-1])))
		
	solutions = solve_poly_system(equation_list, equation_variables)
	
	return solutions[0]

def solve_quadratic_equation(a,b,c):
	root = ((b**2) - (4*a*c))
	if root < 0:
		return -1, -1
	else:
		x1 = ((-b + math.sqrt(root))/(2*a))
		x2 = ((-b - math.sqrt(root))/(2*a))
		return x1,x2

def main():

	n = eval(raw_input("\nEnter number of numbers in array\n"))
	k = eval(raw_input("\nEnter number of missing numbers\n"))
	print ("\n\n")
	
	try:
		number_array = random.sample(range(1, n+1), (n-k))
	except ValueError:
		print ("Invalid values entered")
	
	if (n < 100):
		print ("Numbers: " + str(number_array))
	
	if (k == 1):
		missing_num = find_1_missing(n, number_array)
		print ("Missing Number:   " + str(missing_num) + "\n\n")
		print (number_array)
		
	if (k == 2):
		missing_nums = find_2_missing(n, number_array)
		print ("Missing Numbers:  " + str(int(missing_nums[0])) + ", " + str(int(missing_nums[1])) + "\n\n")
		# print number_array

	if (k == 3):
		missing_nums = find_3_missing(n, number_array)
		print ("Missing Numbers: " + str(int(missing_nums[0])) + ", " + str(int(missing_nums[1])) + ", " + str(int(missing_nums[2])) + "\n\n")

	if (k > 3):
		missing_nums = find_k_missing(n, number_array, k)
		output_string = ""
		for num in missing_nums:
			output_string += str(num) + ", "
		print ("Missing Numbers: " + output_string[0:(len(output_string)-2)])
if __name__ == "__main__":
	main()
