
# Function to add two number
def cal(a,b):
    return a+b

print(cal(2,3))
print(cal(20,3))

# Function to find avg of 3 number
def avg(a,b,c):
    return (a+b+c)/2

print(avg(2,1,3))

# built in function

print("hello", end="-")
print("world")

# function with default values : default values should always be the last parameter if we pass one argument and not pass arguement for other parameter

def prod(a,b=1):
    return a*b
print(prod(4)) # here we pass 4 as value for a and b has default value = 1 but if we want to pass 4 as value for b then we should write def prod(b,a=1) . #! default values should always be the last parameter

