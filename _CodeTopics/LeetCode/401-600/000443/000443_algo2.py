class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        # 还是得写个原地的算法

        length = len(chars)
        if length == 1:
            return 1

        removeSymbol = 0 

        ptrLetter, ptrNum = 0, 1
        while ptrNum < length:
            while ptrNum < length and chars[ptrNum] == chars[ptrLetter]:
                ptrNum += 1
            distance = ptrNum - ptrLetter
            if distance == 1:
                ptrLetter += 1
                ptrNum += 1
                continue
            s = str(distance)
            for i in range(ptrLetter+1, ptrNum):
                if i - ptrLetter <= len(s):
                    chars[i] = s[i-ptrLetter-1]
                else:
                    chars[i] = removeSymbol
            ptrLetter = ptrNum
            ptrNum += 1
        
        distance = ptrNum - ptrLetter
        s = str(distance)
        for i in range(ptrLetter+1, ptrNum):
            if i - ptrLetter < len(s):
                chars[i] = s[i-ptrLetter-1]
            else:
                chars[i] = removeSymbol
        
        while removeSymbol in chars:
            chars.remove(removeSymbol)
        return len(chars)
        
"""
https://leetcode-cn.com/submissions/detail/209584171/

70 / 70 个通过测试用例
状态：通过
执行用时: 348 ms
内存消耗: 13.3 MB

执行用时：348 ms, 在所有 Python 提交中击败了8.79%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了28.57%的用户
"""
