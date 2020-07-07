x = [1, 2, 3, 4, 5, 6]
print (len(x))
## Gives the number of objects in a list


## slices the list into only showing the last three object
print(x[3:])
##prints first three elements of the list
print(x[:3]) 
##prints the last two elements of the list   
print(x[-2:])

##extends the list by adding on to the new list at the end of the orioginal 
x.extend([7,8])
print(x)

##ads a single element ot the end of the original list
x.append(9)
print(x)

##you can make lists of lists just like you can make groups of groups lol group theory 
y = [10,11,12]
listofLists = [x,y]
print(listofLists)

##returns an element of a list 
print(y[1])

##sorts a list in numerical order 
z = [3,2,1,4]
z.sort()
print(z)

##reverse sorts a list
z.sort(reverse = True)
print(z)

##tuples are immutable list, they cannot be changed and they are what they are
a = (1,2,3)
print(len(a))

##list of tuples
b = (4,5,6)
listOfTuples = [a,b]
print(listOfTuples)

##creates a tuple from two comma deliminated numbers and assigns them to two variables
(age, income) = "32,120000".split(',')
print (age)
print (income)
