
`995. K 连续位的最小翻转次数` https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/k-lian-xu-wei-de-zui-xiao-fan-zhuan-ci-s-bikk/
- [x] 方法一：差分数组
- [x] 方法二：滑动窗口

差分思想以及滑动窗口（数据还原问题），附差分相关练习 https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/k-lian-xu-wei-de-zui-xiao-fan-zhuan-ci-s-dseq/

【相信科学系列】朴素贪心解法与贪心差分解法 https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/po-su-tan-xin-jie-fa-yu-tan-xin-chai-fen-4lyy/
- > 结果测试 C++、Python 超时，只有 Java 能过。同样是 97 号样例数据，提交给 LeetCode 执行。Java 运行 200 ms 以内，而 C++ 运行 600 ms。

# 测试用例

```
[0,1,0]
1
[1,1,0]
2
[0,0,0,1,0,1,1,0]
3
```

# 差分数组相关

前缀和 & 差分 https://oi-wiki.org/basic/prefix-sum/

小而美的算法技巧：差分数组 https://labuladong.gitee.io/algo/2/21/54/
