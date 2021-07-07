class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        # 双指针（滑动窗口）
        """
        [1,0,1,0,1]
        2
        [0,0,0,0,0]
        0
        [0,1,0,1,0,1,0,0,0,1,1,1]
        3
        """
        # `TODO`: 该代码有问题，上面的三个测试用例只有第一个能过。但是TMD太困了，眼睛都睁不开了，明天还要上班，直接提交了回来再看了。

        def get_prefix_sum(nums):
            res = [nums[0]]
            for i in range(1, len(nums)):
                res.append(res[-1] + nums[i])
            return res
        prefixSum = get_prefix_sum(nums)

        length = len(nums)
        res = 0
        left = right = 0
        for i in range(goal, length):
            if prefixSum[i] == goal:
                right = i
                res += 1
                break
        
        left += 1
        right += 1
        while left < length - goal and right < length:
            while nums[left] == 0:
                res += 1
                left += 1
                if left == length - goal:
                    break
            while nums[right] == 0:
                res += 1
                right += 1
                if right == length:
                    break
            res += 1
            left += 1
            right += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/193436251/

7 / 60 个通过测试用例
状态：解答错误

最后执行的输入：
[0,0,0,0,0]
0
输出：
10
预期结果：
15
"""
