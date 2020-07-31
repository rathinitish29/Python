#name.count(name[i])
name = input('Enter your name :')
i = 0
b = ''
while i < len(name):
    if name[i] not in b:
        b += name[i]
        print(f' {name[i]} : {name.count(name[i])}')
    i +=1
