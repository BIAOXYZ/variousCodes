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
        return res
    
"""
https://leetcode-cn.com/submissions/detail/109631954/

68 / 82 个通过测试用例
状态：解答错误
"""
"""
注：低级错误，又是忘了模掉 10**9 + 7
"""
