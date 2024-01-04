#Question: Write a program that calculates and prints the value according to the given formula: 
# Q = Square root of [(2 * C * D)/H] 
# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Example Let us assume the following comma separated input sequence is given to the program: 
# 100,150,180 
# The output of the program should be: 18,22,24

#Hints: If the output received is in decimal form, it should be rounded off to its nearest value 
# (for example, if the output received is 26.0, it should be printed as 26) 
# In case of input data being supplied to the question, it should be assumed to be a console input.
print("\nQuestion 6\n")

import math 
def getQ(d:int):
    c = 50
    h = 30
    op = ((2*c*d)/h)
    return round(math.sqrt(op))

values="18,22,24"
l=values.split(",")
res = []
for i in l:
    res.append(getQ(int(i)))
print(*res, sep=",")


#Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j. 
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 
# 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

#Hints: Note: In case of input data being supplied to the question, 
# it should be assumed to be a console input in a comma-separated form.
print("\nQuestion 7\n")