
`474. 一和零` https://leetcode-cn.com/problems/ones-and-zeroes/solution/yi-he-ling-by-leetcode-solution-u2z2/
- [x] 方法一：动态规划
  * > 由此可以得到空间复杂度为 `O(lmn)` 的实现。
  * > 由于 `dp[i][][]` 的每个元素值的计算只和 `dp[i−1][][]` 的元素值有关，因此可以使用滚动数组的方式，去掉 dp 的第一个维度，将空间复杂度优化到 `O(mn)`。
    + > 实现时，内层循环需采用倒序遍历的方式，这种方式保证转移来的是 `dp[i−1][][]` 中的元素值。

# 测试用例

```
["10","0001","111001","1","0"]
5
3
["10", "0", "1"]
1
1
```
