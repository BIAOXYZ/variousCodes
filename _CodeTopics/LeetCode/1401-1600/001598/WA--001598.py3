class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        curPos = 0
        for log in logs:
            if log == "../":
                curPos -= 1
            elif log == "./":
                continue
            else:
                curPos += 1
        return 0 if curPos <= 0 else curPos
        
"""
https://leetcode.cn/submissions/detail/360885808/

68 / 99 个通过测试用例
状态：解答错误
输入：
["./","wz4/","../","mj2/","../","../","ik0/","il7/"]
输出：
1
预期结果：
2
"""
