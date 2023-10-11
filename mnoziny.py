(sm := set(range(0,5)))
{0, 1, 2, 3, 4}
sm.add(20)
sm
{0, 1, 2, 3, 4, 20}
sm.discard(5)
sm
{0, 1, 2, 3, 4, 20}
sm.remove(0)
sm
{1, 2, 3, 4, 20}
###
def si():
    global sa,sb,s2,s3,ra,rb,r2,r3,ta,tb,t2,t3
    sa = {1,2,3,4}; ra = (1,5);     ta = tuple(ra)
    sb = {1,2,3,4}; rb = (1,5);     tb = tuple(rb)
    s2 = {2,4,6,8}; r2 = (2,9,2);   t2 = tuple(r2)
    s3 = {3,6,9};   r3 = (3,10,3);  t3 = tuple(r3)

si()
print((sa,sb,s2,s3),(ta,tb,t2,t3), sep='\n')

