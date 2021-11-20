class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        def list_to_dic_v2(lis):
            dic = {}
            for elem in lis:
                dic[elem] = dic.setdefault(elem, 0) + 1
            return dic
        """
        
        # 今天（2021.11.20）突然想到 `.setdefault()` 方法直接用 `.get()` 也能达到效果。
        # 当然实际的“原理”还是不太一样：
        ## 前者加key的时候，其实是在 `.setdefault()` 部分加的；
        ## 后者加key的时候，其实是在 `dic[elem] = ` 这部分加的。
        def list_to_dic_v3(lis):
            dic = {}
            for elem in lis:
                dic[elem] = dic.get(elem, 0) + 1
            return dic
        
        dic = list_to_dic_v3(nums)
        res = 0
        for k, v in dic.items():
            if dic.has_key(k+1):
                res = max(res, v + dic[k+1])
            if dic.has_key(k-1):
                res = max(res, v + dic[k-1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/240558974/

执行用时：244 ms, 在所有 Python 提交中击败了82.73%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了19.09%的用户
通过测试用例：
206 / 206
"""
