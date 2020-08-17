#febonacchi series
#0 1 1 2 3 5 8 13 21 34

def febonacchi_seq(N):
    a = 0
    b = 1
    if N == 1:
        print(a)
    elif N == 2:
        print(a,b)
    else:
        print(a,b, end = ' ')
        for i in range (N-2):
            c = a+b
            a = b
            b = c
            print(b , end = ' ')
febonacchi_seq(11)
    
