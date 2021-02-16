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
                        loc = right
                        right = mid - 1
                    elif d[mid] < nums[i]:
                        left = mid + 1
                    else:
                        break
                d[loc] = nums[i]
        return len(d)
        
"""
https://leetcode-cn.com/submissions/detail/146171380/

25 / 54 个通过测试用例
状态：解答错误

输入：
[4,10,4,3,8,9]
输出：
4
预期：
3
"""
