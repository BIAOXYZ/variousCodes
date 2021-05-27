class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 官方解法，利用到了一个位运算的trick：
        # “对于整数 val 二进制的第 i 位，我们可以用代码 (val >> i) & 1 来取出其第 i 位的值”
        
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
        
"""
https://leetcode-cn.com/submissions/detail/181522813/

46 / 46 个通过测试用例
状态：通过
执行用时: 228 ms
内存消耗: 14.1 MB

执行用时：228 ms, 在所有 Python 提交中击败了91.67%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了50.00%的用户
"""
