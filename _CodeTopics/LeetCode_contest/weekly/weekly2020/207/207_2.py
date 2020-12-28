class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        alreadyArr = []
        length = len(s)
        res = [1]
        newwordflag = True
        
        def backtrack(currSubStr, pos):
            if pos == length:
                res[0] = max(res[0], len(alreadyArr))
                return
            for end in range(pos+1,length+1):
                tmp = currSubStr
                currSubStr += s[pos:end]
                if currSubStr not in alreadyArr:
                    newwordflag = True
                    alreadyArr.append(currSubStr)
                    backtrack('', end)
                else:
                    newwordflag = False
                    backtrack(currSubStr, end)
                if newwordflag:
                    alreadyArr.pop()
                currSubStr = tmp
                       
        backtrack('', 0)
        return res[0]
    
"""
https://leetcode-cn.com/submissions/detail/109752151/

94 / 94 个通过测试用例
状态：通过
执行用时: 508 ms
内存消耗: 12.5 MB
"""
