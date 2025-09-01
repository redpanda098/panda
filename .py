#example
def greet(name):  # copy value is here (parameter)
    print("hello", name) #using the copy value
    #defination part

greet("Tanishka")  #real value is passed here (argument) #calling part

#Q)create a function to print the sum of two numbers

def sum(a,b):
    return a+b

ans = sum(3,5)
print(ans) #ideal method

# print(sum(3,5))#shortmethod

#create a function which return muliplication of two number
def multiply(a,b):
    return a*b

ans = multiply(3,4)
print(ans)

# cube 

def cube(a):
    return a*a*a

ans = cube(2)
print(ans)

#::::::::::
def counter(n):
    if n == 0: # base condition
        return
    print("the counter is at :", n)
    counter(n-1) # changing the parameter

counter(10)

#factorial number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example
print(factorial(5))   # Output: 120
