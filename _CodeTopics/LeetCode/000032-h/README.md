
`32. 最长有效括号` https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
- [x] 方法一：动态规划
- 方法二：栈
- 方法三：不需要额外的空间

动态规划思路详解（c++）——32.最长有效括号 https://leetcode-cn.com/problems/longest-valid-parentheses/solution/dong-tai-gui-hua-si-lu-xiang-jie-c-by-zhanganan042/

# 残余代码

```py
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        length = len(s)
        prefixsum = [0]
        for i in range(length):
            value = 1 if s[i] == '(' else -1
            prefixsum.append(prefixsum[-1] + value)
        prefixsum.pop(0)
        print prefixsum

        # 之前想用这种计算并分析“多个连续递减序列”的方式来写，但是没有进一步的思路了，先记一下好了。
        # 输入 ")())))()()()(((())))"
        # 打印 [-1, 0, -1, -2, -3, -4, -3, -4, -3, -4, -3, -4, -3, -2, -1, 0, -1, -2, -3, -4]
        """
```
