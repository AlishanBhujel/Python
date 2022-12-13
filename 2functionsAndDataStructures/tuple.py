myTuple = (4, 'strings', 4.5, True, 4, 1.5, 4)

#Accessing items withon the tuple
print(myTuple[1])

#Determining the type of the tuple
print(type(myTuple))

#Declaring tuple without the parenthesis is possibe but not recommended

#counting the number of occurance of an item within a tuple
print(myTuple.count(4))

#Determining the index of the value within a tuple
print(myTuple.index('strings'))

#Iterating through the tuple
for x in myTuple:
    print('value:', x)

#Tuple values are immutable(values cannot change after assigned)
# myTuple[0] = 5 prints TypeError: 'tuple' object does not support item assignment 

