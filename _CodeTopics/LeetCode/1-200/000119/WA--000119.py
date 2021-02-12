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
        return tmp[-1]
        
"""
https://leetcode-cn.com/submissions/detail/145407697/

33 / 34 个通过测试用例
状态：解答错误

输入：
0
输出：
[1,1]
预期：
[1]
"""
