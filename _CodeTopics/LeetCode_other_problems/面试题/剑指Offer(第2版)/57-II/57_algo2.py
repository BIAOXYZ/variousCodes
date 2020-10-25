from collections import deque
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """

        # 滑动窗口（Sliding Window）方法，其实质（至少从这道题看）还是双指针。
        # 参考： https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
        # 但是这种左闭右开的写法感觉很容易出错。比如右指针明明上来应该指向2才更自然。

        left, right = 1, 1
        sum = 0
        res = []

        while left <= target / 2:
            if sum < target:
                sum += right
                right += 1
            elif sum > target:
                sum -= left
                left += 1
            else:
                tmpList = range(left, right)
                res.append(tmpList)
                sum -= left
                left += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118592783/

32 / 32 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 13 MB

执行用时：72 ms, 在所有 Python 提交中击败了72.35%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了27.55%的用户
"""
