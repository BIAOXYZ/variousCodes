class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        def str_to_dict_v2(s):
            dic = {}
            for ch in s:
                dic[ch] = dic.setdefault(ch, 0) + 1
            return dic
        
        dic1 = str_to_dict_v2(chars)
        res = 0
        for word in words:
            flag = "possible"
            dic = str_to_dict_v2(word)
            for k, v in dic.items():
                if k not in dic1 or v > dic1[k]:
                    flag = "impossible"
                    break
            if flag == "possible":
                res += len(word)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/146261315/

36 / 36 个通过测试用例
状态：通过
执行用时: 220 ms
内存消耗: 14 MB

执行用时：220 ms, 在所有 Python 提交中击败了57.93%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了38.41%的用户
"""
