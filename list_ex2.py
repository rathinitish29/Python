#define a function which will take list as a argument and this function will return
# a reversed list

#example :
#[1,2,3,4,] =====> [4,3,2,1]

#note you simplydo this with reverse method or [::-1]
#but try to do this with the help of append and return method

def rever_num(r):
    rev = []
    for i in range(len(r)):
        pop = r.pop()
        rev.append(pop)
    return rev 
a = [1,2,3,4,5,6]
print(rever_num(a))