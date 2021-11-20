class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def list_to_dic_v2(lis):
            dic = {}
            for elem in lis:
                dic[elem] = dic.setdefault(elem, 0) + 1
            return dic
        
        dic = list_to_dic_v2(nums)
        res = 0
        for k, v in dic.items():
            if dic.has_key(k+1):
                res = max(res, v + dic[k+1])
            if dic.has_key(k-1):
                res = max(res, v + dic[k-1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/240535092/

执行用时：272 ms, 在所有 Python 提交中击败了50.00%的用户
内存消耗：15.6 MB, 在所有 Python 提交中击败了26.36%的用户
通过测试用例：
206 / 206
"""
