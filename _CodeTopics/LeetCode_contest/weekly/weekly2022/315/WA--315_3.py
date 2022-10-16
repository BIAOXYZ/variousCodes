class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        for k in range(num):
            if k + int(str(k)[::-1]) == num:
                return True
        return False
    
"""
https://leetcode.cn/submissions/detail/373424572/

257 / 258 个通过测试用例
状态：解答错误

输入：
0
输出：
false
预期：
true
"""
