
```py
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

ln1 = ListNode(1)
a = ln1
print a.val
print "id(ln1) is: ", id(ln1)
print "id(a) is: ", id(a)
ln1.val = 666
print a.val

print("**************************************************")

ln2 = ListNode(2)
a = ln2
print "id(ln1) is: ", id(ln1)
print "id(a) is: ", id(a)
print "id(ln2) is: ", id(ln2)

print("**************************************************")

ln3 = ListNode(3)
ln2.next = ln3
print ln2.next.val

# Although we change "ln3", "ln2.next" does not change!
ln3 = None
print ln2.next.val
ln3 = ListNode(444)
print ln2.next.val

# You cannot directly use "ln3.next" before application a ListNode for it.
ln3.next.val = 555
print ln2.next.val

----------------------------------------------------------------------------------------------------

1
id(ln1) is:  140346077125264
id(a) is:  140346077125264
666
**************************************************
id(ln1) is:  140346077125264
id(a) is:  140346077125328
id(ln2) is:  140346077125328
**************************************************
3
3
3
Traceback (most recent call last):
  File "main.py", line 36, in <module>
    ln3.next.val = 555
AttributeError: 'NoneType' object has no attribute 'val'
```
