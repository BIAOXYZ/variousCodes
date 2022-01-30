class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        # 官方答案，主要是我自己那个忘了用移位，还是用的除2
        ans = 0
        while num:
            ans += num & 1
            if num > 1:
                ans += 1
            num >>= 1
        return ans
        
"""
https://leetcode-cn.com/submissions/detail/263852054/

执行用时：24 ms, 在所有 Python3 提交中击败了97.89%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了62.54%的用户
通过测试用例：
204 / 204
"""
