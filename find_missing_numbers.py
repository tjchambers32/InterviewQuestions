#! python3

import random
import math

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
    squared_number_array = list()
    for num in number_array:
        actual_sum += num
        actual_squared_sum += num**2
        squared_number_array.append(num**2)
    
    # squared_number_array = square(number_array)
    
    # Now set up a system of equations and solve
    # k1 + k2 = x                                    -eq. 1
    # k1**2 + k2**2 = y                      -eq. 2

    x = expected_sum - actual_sum
    y = expected_squared_sum - actual_squared_sum

    return solve_quadratic_equation(1, (x * -1), ((x**2)-y)/2 )


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
    
    try:
        number_array = random.sample(range(1, n+1), (n-k))
    except ValueError:
        print "Invalid values entered"
        
    if (k == 1):
        missing_num = find_1_missing(n, number_array)
        print "Missing Number:   " + str(missing_num) + "\n\n"
        print number_array
        
    if (k == 2):
        missing_nums = find_2_missing(n, number_array)
        print "Missing Numbers:  " + str(int(missing_nums[0])) + ", " + str(int(missing_nums[1])) + "\n\n"
        # print number_array

if __name__ == "__main__":
    main()
