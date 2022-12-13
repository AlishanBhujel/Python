# #global score
globalVariable = 10


# def example1():
#     localVariable = 15
#     print('Accessing the global variable:', globalVariable)

# example1();

#Cannot access the local variable out of its scope
#print('the local variable is:', localVariable)

#Enclosing scope
def example2():
    enclosedVariable = 8

    def example3():
        localVariable = 15
        print('Accessing the global variable:', globalVariable)
        print('Accessing the enclosed variable:', enclosedVariable)
    example3()
    # print('Can not access local variable here')
example2()
# print('can not access enclosed variable here')