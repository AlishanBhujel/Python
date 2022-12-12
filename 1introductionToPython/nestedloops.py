# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8,9]

# count = 0
# #outer loop
# for i in list1:
#     count += 1
#     #inner loop
#     for j in list2:
#        count+=1
# print('The total number of count is:', count)


#Figuring out how long it takes to run my code
import time
start_time = time.time()

for i in range(100):
    for j in range(1000):
        print(0, end = " ") #adding spaces
    print() #new line

print(round(time.time()-start_time,2))