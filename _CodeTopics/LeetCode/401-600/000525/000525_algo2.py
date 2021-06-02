class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 类似 LC523 的思想：哈希表 + 前缀和

        def lambdafunc(b):
            if b == 0:
                return b-1
            return b
        nums = map(lambdafunc, nums)

        length = len(nums)
        res = 0
        prefixSum = [nums[0]]
        # 昨天写的 LC523 （`000523_algo2.py`） 这里字典值用的是list。
        # 今天写时候想了想（至少这道题）不需要，只要保留最小的（也就是第一个出现的）index就行。
        dic = {nums[0]:0}

        for i in range(1, length):
            prefixSum.append(prefixSum[-1] + nums[i])
            if prefixSum[i] == 0:
                res = max(res, i+1)
            if dic.has_key(prefixSum[i]):
                res = max(res, i - dic[prefixSum[i]])
            else:
                dic[prefixSum[i]] = i
        return res
        
"""
https://leetcode-cn.com/submissions/detail/183469253/

564 / 564 个通过测试用例
状态：通过
执行用时: 276 ms
内存消耗: 18.7 MB

执行用时：276 ms, 在所有 Python 提交中击败了72.92%的用户
内存消耗：18.7 MB, 在所有 Python 提交中击败了10.42%的用户
"""
