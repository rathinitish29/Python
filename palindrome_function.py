#palindrome - word that reads same backwards as forwards
# for ex - madam - palindrome

def palindrome (word):
    aword = word[::-1]
    if word == aword:
        return True 
a= (input('Enter any word :'))

print(palindrome(a))

            
