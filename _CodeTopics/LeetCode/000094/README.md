

# `WA--000094_impl2.py`

- 【1】 为什么某些测试用例下，执行代码返回结果正确，但提交解答却出错了 https://support.leetcode-cn.com/hc/kb/article/1194344/
- 【2】 https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000104/000104_impl.py
```py
class Solution(object):
    maxdep = currdep = 0
```
- 【3】 https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000114/000114.py
```py
class Solution(object):
    rightChildrenStack = []
```

参考上面的链接，就知道为啥`WA--000094_impl2.py`错了——其实也没错，是leetcode对全局变量和类内变量（也就是类成员变量）支持太差了。

但是我比较奇怪的一点是：类似【2】的用法我以前也不止一次用，都能对的。如果说是因为【2】里面的类内变量`maxdep`或`currdep`都是普通变量，但是`WA--000094_impl2.py`里的类内变量`res`是个list。但是【3】里的`rightChildrenStack`也是list啊。。。回头再仔细分析下具体代码好了。
