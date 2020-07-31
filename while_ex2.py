number = input('Enter any no to get its digit sum :')
total = 0
i = 0
while i < len(number) :
    total += int(number[i])
    i += 1
    print(total)
