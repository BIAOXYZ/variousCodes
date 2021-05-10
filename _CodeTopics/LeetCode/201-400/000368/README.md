
`368. 最大整除子集` https://leetcode-cn.com/problems/largest-divisible-subset/solution/zui-da-zheng-chu-zi-ji-by-leetcode-solut-t4pz/
- > 这两点揭示了当前问题状态转移的特点，因此可以使用动态规划的方法求解。题目只要求我们得到多个目标子集的其中一个，根据求解动态规划问题的经验，我们需要将子集的大小定义为状态，然后根据结果倒推得到一个目标子集。事实上，当前问题和使用动态规划解决的经典问题「300. 最长递增子序列」有相似之处。
- [x] 方法一：动态规划

# 测试用例

```
[1,2,3]
[1,2,4,8]
[1]
```