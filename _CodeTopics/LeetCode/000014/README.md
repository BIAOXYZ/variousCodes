
最长公共前缀 https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
- 方法一：横向扫描
- 方法二：纵向扫描
- 方法三：分治
- 方法四：二分查找

# 方法一：横向扫描

官方答案定义子函数的时候定义成了和主方法平级，于是调用的时候加上了`self.`：`prefix = self.lcp(prefix, strs[i])`。

# 方法二：纵向扫描

`000014.py`和这个类似，不过我的实现每次都把当前合适的单个前缀字符剥离。

另外官方答案里有用到一个python内置函数`any()`：`if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):`

# 方法三：分治

- 官方答案里这次就是把`lcp()`子函数当成主方法内部的一个函数了，这样调用不用加`self.`。
- 这种语法：`return "" if not strs else lcp(0, len(strs) - 1)`

# 方法四：二分查找

官方答案里用到了python的内置函数`all()`：`return all(strs[i][:length] == str0 for i in range(1, count))`
