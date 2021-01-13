class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """

        length = len(A)
        res = [True] if A[0] == 0 else [False]
        currSum = A[0]

        for i in range(1, length):
            currSum = currSum * 2 + A[i]
            if currSum % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/138219925/

24 / 24 个通过测试用例
状态：通过
执行用时: 352 ms
内存消耗: 14.5 MB

执行用时：352 ms, 在所有 Python 提交中击败了52.24%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了31.34%的用户
"""
