class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        def str_to_dict_v2(s):
            res = {}
            for ch in s:
                res[ch] = res.setdefault(ch, 0) + 1
            return res
        
        dic = str_to_dict_v2(s)
        keys = dic.keys()
        keys.sort(key = lambda x : dic[x], reverse=True)
        
        s = ''
        for key in keys:
            s += key * dic[key]
        return s
        
"""
https://leetcode-cn.com/submissions/detail/191861163/

32 / 32 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 14.9 MB

执行用时：40 ms, 在所有 Python 提交中击败了87.01%的用户
内存消耗：14.9 MB, 在所有 Python 提交中击败了68.36%的用户
"""
