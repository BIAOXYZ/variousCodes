class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
             
        dic = {}
        for request in requests:                
            for i in range(request[0], request[1]+1):
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
        
        valueArr = dic.values()
        valueArr.sort(reverse=True)
        nums.sort(reverse=True)
        
        res = 0
        length = min(len(nums), len(valueArr))
        for i in range(length):
            res += nums[i] * valueArr[i]
        return res % (10**9 + 7)
    
"""
https://leetcode-cn.com/submissions/detail/109632551/

73 / 82 个通过测试用例
状态：超出时间限制
"""
