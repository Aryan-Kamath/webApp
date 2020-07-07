def SquareIt(x):
    return x *x

print(SquareIt(4))

#You can pass functions around as parameters
def DoSomething(f, x):
    return f(x)
print (DoSomething(SquareIt, 3))

#Lambda functions let you inline simple functions
print (DoSomething(lambda x: x * x * x, 3))

##Basic if else loop
if 1 is 3:
    print("How did that happen?")
elif 1 > 3:
    print ("Yikes")
else:
    print ("All is well with the world")

##Looping
for x in range(10):
    print(x)

x = 0
while(x < 10):
    print(x)
    x += 1