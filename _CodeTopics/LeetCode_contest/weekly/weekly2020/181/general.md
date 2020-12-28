
第 181 场周赛 https://leetcode-cn.com/contest/weekly-contest-181
- 5364. 按既定顺序创建目标数组 https://leetcode-cn.com/contest/weekly-contest-181/problems/create-target-array-in-the-given-order/
- 5178. 四因数 https://leetcode-cn.com/contest/weekly-contest-181/problems/four-divisors/
- 5366. 检查网格中是否存在有效路径 https://leetcode-cn.com/contest/weekly-contest-181/problems/check-if-there-is-a-valid-path-in-a-grid/
- 5367. 最长快乐前缀 https://leetcode-cn.com/contest/weekly-contest-181/problems/longest-happy-prefix/

# 笔记

## 1389

```py
# 创建并初始化一个定长的所有值为None的list
target = [None for i in range(length)]

# 参考 https://blog.csdn.net/songyunli1111/article/details/79476983，也可以用
a=[None]*4
```

## （后来补的各种列表推导式、字典推导式、集合推导式）

`5.1.3. 列表推导式` https://docs.python.org/zh-cn/3/tutorial/datastructures.html#list-comprehensions

一些刷题常用的 python 技巧 https://hzhao.me/2019/08/16/python-leetcode-trick/
>> notes：此外这个帖子里还有关于deque、OrderedDict等的一些内容。
```py
# 1d array
l = [0 for _ in range(len(array)]

# 2d
l = [[0] for i in range(cols) for j in range(rows)]
```

```py
# 所以上面那个二维数组的初始化其实不对。。。坑。

lenb = 4
lena = 3
dp = [[0] for i in range(lenb + 1) for j in range(lena + 1)]
dp2 = [[0] * (lenb + 1) for _ in range(lena + 1)]
print "dp= ", dp
print "dp2= ", dp2
dp3 = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
print "dp3= ", dp3
print dp2 == dp3
--------------------------------------------------
dp=  [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
dp2=  [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
dp3=  [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
True
```

Python的各种推导式（列表推导式、字典推导式、集合推导式） https://blog.csdn.net/yjk13703623757/article/details/79490476
```py
# 快速更换key和value
mcase = {'a': 10, 'b': 34}
mcase_frequency = {v: k for k, v in mcase.items()}
print(mcase_frequency)

#  Output: {10: 'a', 34: 'b'}
```
