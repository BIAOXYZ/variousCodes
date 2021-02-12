class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        tmp = [[1],[1,1]]
        for i in range(2, rowIndex+1):
            curr = [1]
            for j in range(1, i):
                curr.append(tmp[i-1][j-1] + tmp[i-1][j])
            curr.append(1)
            tmp.append(curr)
        return tmp[rowIndex]
        
"""
https://leetcode-cn.com/submissions/detail/145408716/

34 / 34 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.1 MB
提交时间：2 分钟前

执行用时：24 ms, 在所有 Python 提交中击败了29.36%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了31.79%的用户
"""
