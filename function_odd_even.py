def odd_even(num):
    if num%2 == 0:
        return 'Even'
    return 'Odd'

a = int(input(' Enter any number : '))
print(odd_even(a))
