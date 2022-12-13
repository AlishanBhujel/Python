list1 = [1,2,3,4,5]


# list2 = ['A','B','C','D','E']

# list3 = ['Hello', 1, True, 40.22]

# list4 = [1, [2,3,4], 5, 6]

#Printing out the entire list
print(*list1)

#sep is the separator
print(list1, sep = " ") #Printing it out as same as it is in code

#Inserting into a list
list1.insert(len(list1), 6)
print(*list1)

#Inserting using append

list1.append(7)
print(*list1)

#Inserting using extend
list1.extend([8,9,10])
print(*list1)

#Deletion using pop
list1.pop(9) # 9 is the index number
print(*list1)

#Deletion using del keyword
del list1[8] # 8 is the index number
print(*list1)

#Iterating through a list
for x in list1:
    print('Value:', x)