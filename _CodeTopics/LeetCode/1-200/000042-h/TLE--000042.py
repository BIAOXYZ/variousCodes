class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 暴力解法，每次找到当前索引 i 对应的位置的左边最高的柱子和右边最高的柱子，然后
        # 算出较矮的一个，最后减去当前的柱子（也可能是0，也就是没有柱子）的高度，就是能存的雨水。

        length = len(height)
        res = 0
        for i in range(1, length-1):
            leftMax, rightMax = 0, 0
            # 这里（还有下面那一处for循环）注意当前index i 本身也得算上，否则产生负数的情况。
            ##for j in range(i-1, -1, -1):
            for j in range(i, -1, -1):
                leftMax = max(leftMax, height[j])
            ##for k in range(i+1, length):
            for k in range(i, length):
                rightMax = max(rightMax, height[k])
            res += min(leftMax, rightMax) - height[i]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/234901240/

318 / 320 个通过测试用例
状态：超出时间限制
"""
