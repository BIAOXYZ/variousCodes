
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

```py
#// 参考：《一些刷题常用的 python 技巧》 https://hzhao.me/2019/08/16/python-leetcode-trick/
#// 此外这个帖子里还有关于deque、OrderedDict等的一些内容。

# 1d array
l = [0 for _ in range(len(array)]

# 2d
l = [[0] for i in range(cols) for j in range(rows)]
```
