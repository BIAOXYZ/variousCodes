
最长公共前缀 https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
- 方法一：横向扫描
- 方法二：纵向扫描
- 方法三：分治
- 方法四：二分查找

## 方法二：纵向扫描

`000014.py`和这个类似，不过我的实现每次都把当前合适的单个前缀字符剥离。

另外官方答案里有用到一个python内置函数`any()`：`if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):`
