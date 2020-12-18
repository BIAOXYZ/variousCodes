class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def str_to_dict(s):
            dic = {}
            for ch in s:
                if ch in dic:
                    dic[ch] += 1
                else:
                    dic[ch] = 1
            return dic
        
        dicS, dicT = str_to_dict(s), str_to_dict(t)
        for k, v in dicT.items():
            # 第一次没把这俩条件写成一句主要是为了试试别的语言里的 elif/else if。
            if k not in dicS or v > dicS[k]:
                return k
        
"""
https://leetcode-cn.com/submissions/detail/131939881/

54 / 54 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13 MB

执行用时：28 ms, 在所有 Python 提交中击败了51.77%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了23.77%的用户
"""
