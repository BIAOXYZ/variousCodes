class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        # 单调栈算法，同样参考官方答案的思想。

        if not num:
            return '0'
        num, length = list(num), len(num)
        stk = [num[0]]

        for i in range(1, length):
            if int(num[i]) >= int(stk[-1]):
                stk.append(num[i])
            else:
                while stk and int(num[i]) < int(stk[-1]) and k > 0:
                    stk.pop()
                    k -= 1
                stk.append(num[i])
        
        while k > 0:
            stk.pop()
            k -= 1
        while stk and stk[0] == '0':
            stk.pop(0)
        if not stk:
            return '0'
        return ''.join(stk)
        
"""
https://leetcode-cn.com/submissions/detail/123656366/

33 / 33 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 13.8 MB

执行用时：68 ms, 在所有 Python 提交中击败了13.51%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了5.09%的用户
"""
