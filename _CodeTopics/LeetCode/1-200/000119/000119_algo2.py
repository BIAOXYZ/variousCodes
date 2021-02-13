class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]

        last = [1,1]
        for i in range(2, rowIndex+1):
            curr = [1]
            for j in range(1, i):
                curr.append(last[j-1] + last[j])
            curr.append(1)
            last = curr
        return last
        
"""
https://leetcode-cn.com/submissions/detail/145561530/

34 / 34 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB

执行用时：20 ms, 在所有 Python 提交中击败了53.94%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了37.31%的用户
"""
