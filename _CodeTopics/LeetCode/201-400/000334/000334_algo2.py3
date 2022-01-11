class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # 这个是 `LC300. 最长递增子序列` 里的第二种方法：贪心 + 二分查找。

        length = len(nums)
        d = [nums[0]]

        for i in range(1, length):
            if nums[i] > d[-1]:
                d.append(nums[i])
                if len(d) >= 3:
                    return True
            else:
                loc = bisect.bisect_left(d, nums[i])
                d[loc] = nums[i]
        return False
        
"""
https://leetcode-cn.com/submissions/detail/257494758/

执行用时：124 ms, 在所有 Python3 提交中击败了15.11%的用户
内存消耗：24.1 MB, 在所有 Python3 提交中击败了16.17%的用户
通过测试用例：
76 / 76
"""
"""
参考了： https://leetcode-cn.com/submissions/detail/151173818/
"""
