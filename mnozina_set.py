s0 = set(); print(s0, type(s0))
#
set('python') #IDLE
#
for c in set('python'): print(c, hash(c)%32, sep=':', end=' ')
