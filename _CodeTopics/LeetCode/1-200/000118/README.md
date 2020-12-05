
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

第`22`行`res.append(newList)`，等提交了才发现：按理说为了保证不影响后面，这里更准确的不应该是`res.append(newList[:])`吗？然后试了一下，发现python的list一旦赋值成空list，应该就算“销毁”然后重新申请了吧？

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
