class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # 滑动窗口实现 —— 类似官方答案。
        # 官方答案对集合开始的处理比较优雅：不是先一次生成，而是一个一个来。
        se = set()
        for i in range(len(nums)):
            if i >= k+1:
                se.remove(nums[i-k-1])
            if nums[i] in se:
                return True
            se.add(nums[i])
        return False
        
"""
https://leetcode-cn.com/submissions/detail/260013236/

执行用时：88 ms, 在所有 Python3 提交中击败了51.37%的用户
内存消耗：23 MB, 在所有 Python3 提交中击败了72.87%的用户
通过测试用例：
51 / 51
"""
