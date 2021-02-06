class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def list_to_dic(lis):
            dic = {}
            for elem in lis:
                if elem in dic:
                    dic[elem] += 1
                else:
                    dic[elem] = 1
            return dic
        
        dic = list_to_dic(nums)
        res = 0
        for k, v in dic.items():
            if v == 1:
                res += k
        return res
    
"""
https://leetcode-cn.com/contest/biweekly-contest-45/submissions/detail/144244758/ # 被第二道题给气的，不小心关了，发现还有这个链接可以查提交，但是没有详情。

https://leetcode-cn.com/submissions/detail/144244758/

73 / 73 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB
"""
