class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        def str_to_dict_index(s):
            dic = {}
            for i, ch in enumerate(s):
                if dic.has_key(ch):
                    dic[ch].append(i)
                else:
                    dic[ch] = [i]
            return dic
        
        dic = str_to_dict_index(s)
        keys = dic.keys()
        keys.sort()
        
        prevInd = []
        for ch in keys:
            indSet = dic[ch]
            if not prevInd:
                prevInd.append(indSet[0])
                continue
            if len(indSet) == 1:
                prevInd.append(indSet[0])
            else:
                if indSet[-1] < min(prevInd):
                    prevInd.append(indSet[0])
                else:
                    i = 0
                    while indSet[i] < min(prevInd):
                        i += 1
                    prevInd.append(indSet[i])

        res = ""
        for ind in sorted(prevInd):
            res = res + s[ind]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/132360684/

243 / 289 个通过测试用例
状态：解答错误

输入：
"leetcode"
输出：
"ltcode"
预期：
"letcod"
"""
