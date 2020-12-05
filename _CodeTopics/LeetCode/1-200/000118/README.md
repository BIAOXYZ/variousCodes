
`118. 杨辉三角` https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-by-leetcode-solution-lew9/
- [x] 方法一：数学

# 测试用例

```
5
1
2
0
```

# 语法点

## `000118.py`

第`22`行`res.append(newList)`，等提交了才发现：按理说为了保证不影响后面，这里更准确的不应该是`res.append(newList[:])`吗？然后试了一下，发现python的list一旦赋值成空list，应该就算“销毁”然后重新申请了吧？(TODO --> Finished)

```py
l = [1,2]
ll = [l]
print ll

l.append(3)
print ll

l = []
print ll

l.append(5)
print ll
--------------------------------------------------
[[1, 2]]
[[1, 2, 3]]
[[1, 2, 3]]
[[1, 2, 3]]
```

后来在如下stackoverflow页面找到了答案：

Different ways of clearing lists https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists
- https://stackoverflow.com/a/850831/10482486
  * > Clearing a list in place will affect all other references of the same list.
  * > For example, this method doesn't affect other references:
    ```py
    >>> a = [1, 2, 3]
    >>> b = a
    >>> a = []
    >>> print(a)
    []
    >>> print(b)
    [1, 2, 3]
    ```
  * > But this one does:
    ```py
    >>> a = [1, 2, 3]
    >>> b = a
    >>> del a[:]      # equivalent to   del a[0:len(a)]
    >>> print(a)
    []
    >>> print(b)
    []
    >>> a is b
    True
    ```
  * > You could also do:
    ```py
    >>> a[:] = []
    ```
  * 然后是有人提问原因，我也是从回答里找到了答案。 
  * > Why the first one will only affect a? I thought a and b reference to the same object... Just wanna know why. Thanks. 
    >> because in first you are changing a reference for 'a' to point to new array, not clearing one, and b still points an old one
  * 评论里还有人提到了python3.3以后可以用`clear()`方法：
  * > With python 3.3 and later you can go with `a.clear()`, no problem! 

>> //notes：于是实验一下上面两个：
```py
a = [1, 2, 3]
b = a
a[:] = []
print(a)
print(b)
--------------------------------------------------
[]
[]
```
```py3
# 注意这个是在python3下进行的。

a = [1, 2, 3]
b = a
a.clear()
print(a)
print(b)
--------------------------------------------------
[]
[]
```

然后发现其实最开头是想错了，不是销毁，就是指向了另一个对象而已：
```py
x = [1, 2, 3]
y = x
x = [8,8]
print(x)
print(y)
----------
[8, 8]
[1, 2, 3]
```
```py
x = [1, 2, 3]
xx = [x]
print x
print xx
x = [8,8]
print x
print xx
----------
[1, 2, 3]
[[1, 2, 3]]
[8, 8]
[[1, 2, 3]]
```
