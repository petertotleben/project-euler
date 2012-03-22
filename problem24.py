def fact(n):
  return reduce(lambda x,y:x*y,range(1,n+1),1)
 
def perm(n, s):
  if len(s)==1: return s
  q, r = divmod(n, fact(len(s)-1))
  return s[q] + perm(r, s[:q] + s[q+1:])
 
print "Answer is {0}".format(perm(999999, '0123456789'))

