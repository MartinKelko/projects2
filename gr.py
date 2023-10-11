def f(a,b=20,*args,c=40):
    print(f'{a=},{b=},{args=},{c=}')

f(1)
f(1,2,3,4,5)
f(a=11)
f(c=44,b=22,a=11)
