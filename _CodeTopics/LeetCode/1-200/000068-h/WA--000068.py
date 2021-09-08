class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        length = len(words)
        res = []
        
        currWordList, currStrLen = [], 0
        i = 0
        while i < length:
            if not currWordList:
                currWordList.append(words[i])
                currStrLen += len(words[i])
                i += 1
            else:
                if currStrLen + len(currWordList) + len(words[i]) > maxWidth:
                    numWhiteSpaces = maxWidth - currStrLen
                    if len(currWordList) == 1:
                        currWordList[0] += " " * numWhiteSpaces
                    else:
                        j = 0
                        while numWhiteSpaces > 0:
                            currWordList[j] += " "
                            numWhiteSpaces -= 1; j = (j + 1) % (len(currWordList) - 1)
                    res.append("".join(currWordList))
                    currWordList, currStrLen = [], 0
                else:
                    currWordList.append(words[i])
                    currStrLen += len(words[i])
                    i += 1
        
        # 处理最后一行
        numWhiteSpaces = maxWidth - currStrLen
        for k in range(len(currWordList)):
            currWordList[k] += " "
            numWhiteSpaces -= 1
        currWordList[-1] += " " * numWhiteSpaces
        res.append("".join(currWordList))

        return res
        
"""
https://leetcode-cn.com/submissions/detail/216960783/

23 / 27 个通过测试用例
状态：解答错误

最后执行的输入：
["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
16
输出：
["ask   not   what","your country can","do  for  you ask","what  you can do","for your country "]
预期结果：
["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"]
"""
