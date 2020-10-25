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

        """
        # 修正上面的做法，改成左闭右闭。此外修改的地方包括：
        # 1. 起始点为[1,2] 
        # 2. 起始和为3
        # 3. sum += right 变为 sum += right + 1
        # 4. tmpList = range(left, right) 变为 tmpList = range(left, right+1)
        """

        left, right = 1, 2
        sum = 3
        res = []

        while left <= target / 2:
            if sum < target:
                sum += right + 1
                right += 1
            elif sum > target:
                sum -= left
                left += 1
            else:
                tmpList = range(left, right+1)
                res.append(tmpList)
                sum -= left
                left += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118592975/

32 / 32 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 13 MB

执行用时：64 ms, 在所有 Python 提交中击败了83.46%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了27.99%的用户
"""
