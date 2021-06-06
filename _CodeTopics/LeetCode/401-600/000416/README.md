
`416. 分割等和子集` https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
- > **前言**
  * > 本题是经典的[NP 完全问题](https://baike.baidu.com/item/NP%E5%AE%8C%E5%85%A8%E9%97%AE%E9%A2%98)，也就是说，如果你发现了该问题的一个[多项式算法](https://baike.baidu.com/item/%E5%A4%9A%E9%A1%B9%E5%BC%8F%E7%AE%97%E6%B3%95)，那么恭喜你证明出了 P=NP，可以期待一下图灵奖了。
  * > 正因如此，我们不应期望该问题有多项式时间复杂度的解法。我们能想到，例如基于贪心算法的「将数组降序排序后，依次将每个元素添加至当前元素和较小的子集中」之类的方法都是错误的，可以轻松地举出反例。因此，我们必须尝试非多项式时间复杂度的算法，例如时间复杂度与元素大小相关的动态规划。
- 方法一：动态规划

一篇文章吃透背包问题！（细致引入+解题模板+例题分析+代码呈现） https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-a7dd/

【宫水三叶/背包问题(上)】如何将原问题抽象为「01 背包」问题 https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/gong-shui-san-xie-bei-bao-wen-ti-shang-r-ln14/

【宫水三叶/背包问题(下)】从「最多不超过」到「恰好」，换个角度来理解「背包问题」 https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/gong-shui-san-xie-bei-bao-wen-ti-xia-con-mr8a/

「代码随想录」帮你把0-1背包学个通透！ https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/bang-ni-ba-0-1bei-bao-xue-ge-tong-tou-by-px33/

# 测试用例

```
[1,5,11,5]
[1,2,3,5]
[1,2]
[1,2,3]
```

# 其他参考链接

背包九讲——全篇详细理解与代码实现 https://blog.csdn.net/yandaoqiusheng/article/details/84782655

背包九讲----整理+例题 https://blog.csdn.net/weixin_43693379/article/details/89432283

0-1 Knapsack Problem | DP-10 https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

0-1背包问题的动态规划算法 - Bat特白的文章 - 知乎 https://zhuanlan.zhihu.com/p/30959069

leetcode题解（0-1背包问题） https://juejin.im/post/6844903634895896583
