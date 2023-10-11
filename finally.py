def demo_finally(arg) -> str:
    sum = f'demo({arg}):'
    def add(a): nonlocal sum; sum += f'({a})'
    try:
        if arg > 0: add('run'); return sum
        elif arg < 0: add ('exc'); raise Exception(sum)
    except Exception as ex:
        add('In exc')
        raise ex
    finally:
        add('In fin')
        if arg in (-1,1):
            add('From fin')
            return sum
    return (f'Outside: {sum}')
for i in range(2,-3,-1): print(demo_finally(i))
