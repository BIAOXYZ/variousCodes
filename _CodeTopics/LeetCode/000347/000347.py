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
        """
        # 淦，这都能中招。。。对第一组输入来说，这里的k估计跟输入参数k冲突了。导致我顺手把最后
        # `for i in range(k):` 里的k改成了k-1，当时也觉得不对，应该是k呀。
        for k, v in dic.items():
            lis.append([k,v])
        """
        for key, val in dic.items():
            lis.append([key,val])

        def take_second(item):
            return item[1]
        lis.sort(key=take_second, reverse=True)

        res = []
        for i in range(k):
            res.append(lis[i][0])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/105777175/

21 / 21 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15.9 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了81.34%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了9.63%的用户
"""
