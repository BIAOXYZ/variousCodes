class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        # 贪心算法思想：每次去掉一个，循环k次。
        num = list(num)
        for i in range(k):
            j = 0
            while j <= len(num) - 2 and num[j] <= num[j+1]:
                j += 1
            if j < len(num) - 1:
                num.pop(j)
            else:
                num.pop()

        while num and num[0] == '0':
            num.pop(0)
        if not num:
            return '0'
        return ''.join(num)
        
"""
https://leetcode-cn.com/submissions/detail/123644972/

33 / 33 个通过测试用例
状态：通过
执行用时: 396 ms
内存消耗: 13.5 MB

执行用时：396 ms, 在所有 Python 提交中击败了5.40%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了14.35%的用户
"""
