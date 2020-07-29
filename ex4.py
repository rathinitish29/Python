name,letter= input('Enter comma separated your name and letter :').split(',')
print(f'length of your name is {len(name)}')
print(f'character count : {name.lower().count(letter.lower())}')
