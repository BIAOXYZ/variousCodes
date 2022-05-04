class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # 这个题是一个能说明 “滑动窗口是双指针的一种特例” 的好例子。 --> 有点绕口。。。

        n = len(nums)
        left, right = 0, 0
        product = 1
        res = 0
        while right < n and left <= right:
            product *= nums[right]
            if product < k:
                res += 1
                right += 1
            else:
                while product >= k and left <= right:
                    product //= nums[left]
                    left += 1
                res += right - left + 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/309243661/

4 / 97 个通过测试用例
状态：解答错误

输入：
[1,1,1]
2
输出：
3
预期结果：
6
"""
