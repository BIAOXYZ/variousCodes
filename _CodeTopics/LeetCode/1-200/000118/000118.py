class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = []
        for rowId in range(1, numRows+1):
            if rowId == 1:
                res.append([1])
            elif rowId == 2:
                res.append([1,1])
            else:
                lastList, newList = res[-1], []
                for i in range(rowId - 1):
                    if i == 0:
                        newList.append(lastList[0])
                    else:
                        newList.append(lastList[i] + lastList[i-1])
                newList.append(lastList[-1])
                res.append(newList)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/128899592/

15 / 15 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.8 MB

执行用时：16 ms, 在所有 Python 提交中击败了76.48%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了42.27%的用户
"""
