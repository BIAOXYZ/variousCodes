
```py
t = (1,2,3,4)
l = [1,2,3,4,3]
d = {1:2,3:4}
s1 = set(t)
s2 = set(l)
s3 = set(d)
print "original tuple is: ", t
print "original list is: ", l
print "original dictionary is: ", d
print "set from tuple is: ", s1
print "set from list is: ", s2
print "set from dictionary is: ", s3

l = set(l)
print "yes, we can directly assign set to list: ", l
--------------------------------------------------
original tuple is:  (1, 2, 3, 4)
original list is:  [1, 2, 3, 4, 3]
original dictionary is:  {1: 2, 3: 4}
set from tuple is:  set([1, 2, 3, 4])
set from list is:  set([1, 2, 3, 4])
set from dictionary is:  set([1, 3])
yes, we can directly assign set to list:  set([1, 2, 3, 4])
```
