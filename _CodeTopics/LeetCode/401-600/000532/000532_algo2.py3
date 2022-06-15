import bisect
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        res = 0
        i, j = 0, 0
        while i < n and j < n:
            # 这个写法挺好的，可以一直保持 j 处在 i 前面（且不相等）的位置。
            if i >= j:
                j += 1
                continue
            if nums[i] + k < nums[j]:
                i += 1
            elif nums[i] + k > nums[j]:
                j += 1
            else:
                res += 1
                i += 1
                while i < n and nums[i] == nums[i-1]:
                    i += 1
                # 有了上面那个写法，下面这两句也不用了。
                # while j < n and nums[j] == nums[j-1]:
                #     j += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/325728864/

执行用时：
52 ms
, 在所有 Python3 提交中击败了
48.42%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
92.98%
的用户
通过测试用例：
60 / 60
"""
