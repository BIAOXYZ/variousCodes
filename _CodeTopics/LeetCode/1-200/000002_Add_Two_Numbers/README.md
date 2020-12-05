
`2. 两数相加` https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode-solution/
- [x] 方法一：模拟

# `000002_Add_Two_Numbers_algo1.py`

>> //notes：其实仔细理一理就清楚了：`ln2.next`归根到底其实质也就是一个`ListNode`类型的`node`。我先把`ln3`赋给这个`node`，然后`ln3`设为`None`，这里改变的是`ln3`啊，`node`**并没有被再次赋值**，所以当然不会改变。
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

# You cannot directly use "ln3.next" before applying a ListNode for it.
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
>> 【[:star:][`*`]】 //notes：注：结合`LC118`的[`README`](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/1-200/000118/README.md)看更容易明白，在那里针对list类型做了更多的总结。
