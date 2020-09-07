class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        length = len(nums)

        dic = {}
        for i in range(length):
            if dic.has_key(nums[i]):
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        if len(dic) == 1:
            return [nums[0]]

        lis = []
        for k, v in dic.items():
            lis.append([k,v])

        def take_second(item):
            return item[1]
        lis.sort(key=take_second, reverse=True)

        res = []
        for i in range(k-1):
            res.append(lis[i][0])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/105774731/

3 / 21 个通过测试用例
状态：解答错误

输入：[1,2]
     2
输出：[1]
预期：[1,2]
"""
