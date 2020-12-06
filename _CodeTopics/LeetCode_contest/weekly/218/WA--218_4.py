class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        dic = {}
        for num in nums:
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
        maxFreq = max(dic.values())
        if maxFreq > k:
            return -1
        
        length = len(nums)
        cardinality = length / k
        nums.sort()
        
        lists = [[] for i in range(k)]
        startindex = 0
        for num in nums:
            while len(lists[startindex]) == cardinality:
                startindex += 1
            index = startindex
            while num in lists[index]:
                index = (index + 1) % k
            lists[index].append(num)
        print lists
        
        res = 0
        for lis in lists:
            res += lis[-1] - lis[0]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/128962494/

47 / 53 个通过测试用例
状态：解答错误

输入：
[6,3,8,1,3,1,2,2]
4
输出：
10
预期：
6
"""
