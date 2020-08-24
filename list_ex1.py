#define a function which will take list containing numbers as input and return list
#  containing square of every elements
# 
# example 
# numbers = [1,2,3,4]
# square_list(numbers ) = return ===> [1,4,9,16]

def square_list(l):
    squar = []
    for i in l:
        squar.append(i**2)
    return squar

num = list(range(1,11))    
print(square_list(num))
    
