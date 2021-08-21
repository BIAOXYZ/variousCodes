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
                    chars[i] = "$"
            ptrLetter = ptrNum
            ptrNum += 1
        
        distance = ptrNum - ptrLetter
        s = str(distance)
        for i in range(ptrLetter+1, ptrNum):
            if i - ptrLetter < len(s):
                chars[i] = s[i-ptrLetter-1]
            else:
                chars[i] = "$"
        
        while "$" in chars:
            chars.remove("$")
        return len(chars)
        
"""
https://leetcode-cn.com/submissions/detail/209581653/

43 / 70 个通过测试用例
状态：解答错误

最后执行的输入：
["y","(","V","t","l","]","&","'","T","$"]
输出：
["y","(","V","t","l","]","&","'","T"]
预期结果：
["y","(","V","t","l","]","&","'","T","$"]
"""
"""
艹，没看到输入里可能有符号。。。服了！
"""
