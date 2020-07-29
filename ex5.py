winning_num= int('7')
guess = int(input('guess any number b/w 1-100 : '))
if winning_num == guess:
    print('you won ')

else:
    if guess >= winning_num :
        print('high')
        print('you lost')
    if guess <= winning_num :
        print('less')
        print('you lost')
