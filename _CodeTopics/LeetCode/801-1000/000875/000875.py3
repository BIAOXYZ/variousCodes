class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # 经典的二分查找应用类题目。

        def calculate_time(k):
            res = 0
            for pile in piles:
                res += pile // k + 1 * int(pile % k != 0)
            return res
        
        # 这里 minK 应该用 1 更好，但是 0 应该也没问题，打算先试试。
        # 用 0 会 RE。。。ZeroDivisionError。。。
        minK, maxK = 1, max(piles)
        res = maxK
        while minK <= maxK:
            mid = minK + (maxK - minK) // 2
            if calculate_time(mid) < h:
                # 这里只要当前需要时间比 h 小，就可以更新答案了，所以实际上和
                # calculate_time(mid) 等于 h 的情况所采用的处理方式是一致的。
                # 但是还是不合并了，方便后面回顾时看。
                res = mid
                maxK = mid - 1
            elif calculate_time(mid) > h:
                minK = mid + 1
            else:
                res = mid
                maxK = mid - 1
        return res
        
"""
https://leetcode.cn/submissions/detail/322435087/

执行用时：
544 ms
, 在所有 Python3 提交中击败了
11.02%
的用户
内存消耗：
16.2 MB
, 在所有 Python3 提交中击败了
46.03%
的用户
通过测试用例：
121 / 121
"""
