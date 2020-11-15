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

        if not num:
            return '0'
        while num[0] == '0':
            num.pop(0)
        return ''.join(num)
        
"""
https://leetcode-cn.com/submissions/detail/123643959/

3 / 33 个通过测试用例
状态：执行出错

执行出错信息：
Line 22: IndexError: list index out of range
最后执行的输入：
"10"
1
"""
