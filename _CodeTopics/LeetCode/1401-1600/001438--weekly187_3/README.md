
`1438. 绝对差不超过限制的最长连续子数组` https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/jue-dui-chai-bu-chao-guo-xian-zhi-de-zui-5bki/
- [x] 方法一：滑动窗口 + 有序集合
  * > 为了方便统计当前窗口内的最大值与最小值，我们可以使用平衡树来维护窗口内元素构成的有序集合。
    + > 语言自带的红黑树，例如 C++ 中的 `std::multiset`，Java 中的 `TreeMap`；
    + > 第三方的平衡树库，例如 Python 中的 `sortedcontainers`（事实上，这个库的底层实现并不是平衡树，但各种操作的时间复杂度仍然很优秀）；
    + > 手写 `Treap` 一类的平衡树，例如下面的 Golang 代码。
- [x] 方法二：滑动窗口 + 单调队列

# 测试用例

```
[8,2,4,7]
4
[10,1,2,4,7,2]
5
[4,2,2,2,4,4,2,2]
0
```

# 备注

此题是之前第187周周赛第三题： https://leetcode-cn.com/contest/weekly-contest-187/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

当时的提交超时了： https://leetcode-cn.com/submissions/detail/67789804/
