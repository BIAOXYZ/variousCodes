class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        state = 0
        total = 0
        for ch in s:
            if ch == "[":
                state += 1
            else:
                state -= 1
                if state < 0:
                    total += 1
        if total % 2 == 1:
            total += 1
        return total >> 1
    
"""
https://leetcode-cn.com/submissions/detail/204523826/

14 / 58 个通过测试用例
状态：解答错误

最后执行的输入：
"][][]["
输入：
"][][]["
输出：
2
预期：
1
"""
