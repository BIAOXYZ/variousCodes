class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 一看就是想考二分，但是头疼的厉害，还是手动狗头一把了。。。
        return collections.Counter(nums)[target] if target in nums else 0
        
"""
https://leetcode-cn.com/submissions/detail/196231284/

88 / 88 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.2 MB

执行用时：28 ms, 在所有 Python 提交中击败了29.08%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了77.77%的用户
"""
