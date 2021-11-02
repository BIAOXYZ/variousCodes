class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 动态规划法，其实就是暴力解法稍微变形：上来把所有位置的leftMax和rightMax都预计算出来，
        # 存到相关数组里，后面循环的时候直接用，不再重复计算。

        length = len(height)
        dpLeftMax = [height[0]] + [-1 for _ in range(length-1)]
        dpRightMax = [-1 for _ in range(length-1)] + [height[-1]]

        for i in range(1, length):
            dpLeftMax[i] = max(dpLeftMax[i-1], height[i])
        for j in range(length-2, -1, -1):
            dpRightMax[j] = max(dpRightMax[j+1], height[j])

        res = sum([min(dpLeftMax[i], dpRightMax[i]) - height[i] for i in range(1, length-1)])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/234902313/

执行用时：36 ms, 在所有 Python 提交中击败了19.93%的用户
内存消耗：14.4 MB, 在所有 Python 提交中击败了5.39%的用户
通过测试用例：
320 / 320
"""
