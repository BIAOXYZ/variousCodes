class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        dic = {1:'1', 2:'11', 3:'21', 4:'1211', 5:'111221'}
        if n in range(1, 6):
            return dic[n]

        currStr = dic[5]
        for _ in range(6, n+1):
            nextStr = ''
            startPos = 0
            for i in range(len(currStr)):
                if i == 0:
                    continue
                else:
                    if currStr[i] != currStr[i-1]:
                        nextStr += str(i - startPos) + currStr[startPos]
                        startPos = i
            nextStr += str(len(currStr) - startPos) + currStr[startPos]
            currStr = nextStr
        return currStr
        
"""
https://leetcode-cn.com/submissions/detail/229013214/

30 / 30 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13 MB

执行用时：12 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了81.54%的用户
"""
