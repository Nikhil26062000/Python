

nums = [1,2,3,4,5]

for num in nums:
    print(num)
else: #optional 
    print("end")


# Range : range(start?, end, step ?)  step by default is 1

for i in range(5):
    print(i)

for i in range(9,15):
    print(i)

for i in range(20,35,2):
    print(i)


# Pass statement : used to leave that block of code 

for i in range(5):
    pass

print("end")

# other example of pass
x=10
if x>5:
    pass