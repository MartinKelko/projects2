def recDemo (n, s=''):

    print(s, '==>', n)
    if n > 0:
        recDemo(n-1, s+' ')
    print(s,n,'<==')

recDemo(5)
