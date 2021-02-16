class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 这个是官方答案贪心 + 二分查找方法的思路，既难想也难以理解。

        length = len(nums)
        d = [nums[0]]

        for i in range(1, length):
            if nums[i] > d[-1]:
                d.append(nums[i])
            else:
                left, right = 0, len(d)-1
                loc = right
                while left <= right:
                    mid = (left + right) / 2
                    if d[mid] > nums[i]:
                        loc = mid
                        right = mid - 1
                    elif d[mid] < nums[i]:
                        left = mid + 1
                    else:
                        loc = mid
                        break
                d[loc] = nums[i]
        #print d
        return len(d)
        
"""
https://leetcode-cn.com/submissions/detail/146173498/

54 / 54 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.5 MB

执行用时：36 ms, 在所有 Python 提交中击败了93.45%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了11.06%的用户
"""
