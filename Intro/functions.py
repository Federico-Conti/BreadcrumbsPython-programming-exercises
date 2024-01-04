def sumTwoNumbers(a, b):
    return a + b

def sumNumbers(*args): #definitio of function with unknown value numbers
    sum_value = 0
    for n in args:
        sum_value += n
    return sum_value

x = 10
y = 20  
sumTwoNumbers(x, y) # 30
sumNumbers(x=x, y=y) # specify the name of the parameters   
sumNumbers(10,20,30) # 60

lambaFun = lambda x,y: x + y
lambdaFun(10,20) # 30