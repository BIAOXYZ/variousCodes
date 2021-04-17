class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # 滑动窗口应该也可以吧，不过先试试排序。--> 但是总体看还是O(n^2)的复杂度，感觉又会超时。。。

        length = len(nums)
        newNums = [[nums[i], i] for i in range(length)]
        newNums.sort(key = lambda x : (x[0], x[1]))

        for i in range(length-1):
            for j in range(i+1, length):
                if newNums[j][0] - newNums[i][0] > t:
                    break
                if abs(newNums[j][1] - newNums[i][1]) <= k:
                    return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/168911142/

54 / 54 个通过测试用例
状态：通过
执行用时: 3952 ms
内存消耗: 19.9 MB

执行用时：3952 ms, 在所有 Python 提交中击败了10.75%的用户
内存消耗：19.9 MB, 在所有 Python 提交中击败了5.37%的用户
"""
