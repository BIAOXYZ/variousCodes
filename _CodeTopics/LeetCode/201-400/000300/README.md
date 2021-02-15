
`300. 最长递增子序列` https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
- [x] 方法一：动态规划
  * > 定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度，**注意 nums[i] 必须被选取**。
- [x] 方法二：贪心 + 二分查找

# 测试用例

```
[10,9,2,5,3,7,101,18]
[0,1,0,3,2,3]
[7,7,7,7,7,7,7]
[1]
[1,2]
[2,1]
```

# `000300.py`

这个和官方答案看起来很相似，但是实际dp数组的意义是不一样的，我觉得我的更好一点。我的 `dp[i]` 的意思是，以位置 `i` 的数开头的最长上升子序列的长度。
