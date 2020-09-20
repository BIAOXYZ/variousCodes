class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # def backtrack(currSubStr, pos):
        
        alreadyArr = []
        length = len(s)
        newwordFlag, currWord = True, ''
        for i in range(length):
            currWord += s[i]
            if currWord not in alreadyArr:
                alreadyArr.append(currWord)
                currWord = ''
        return len(alreadyArr)
    
"""
https://leetcode-cn.com/submissions/detail/109739428/

76 / 94 个通过测试用例
状态：解答错误

输入：
"addbsd"
输出：
4
预期：
5
"""
