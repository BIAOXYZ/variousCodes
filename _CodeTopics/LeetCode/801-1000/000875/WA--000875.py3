class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # 经典的二分查找应用类题目。

        def calculate_time(k):
            res = 0
            for pile in piles:
                res += pile // k + 1 * int(pile % k != 0)
            return res

        minK, maxK = 0, max(piles)
        res = maxK
        while minK <= maxK:
            mid = minK + (maxK - minK) // 2
            if calculate_time(mid) < h:
                maxK = mid - 1
            elif calculate_time(mid) > h:
                minK = mid + 1
            else:
                res = mid
                maxK = mid - 1
        return res
        
"""
https://leetcode.cn/submissions/detail/322434654/

4 / 119 个通过测试用例
状态：解答错误

输入：
[312884470]
312884469
输出：
312884470
预期结果：
2
"""
