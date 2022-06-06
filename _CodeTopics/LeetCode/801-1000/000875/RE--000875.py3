class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # 经典的二分查找应用类题目。

        def calculate_time(k):
            res = 0
            for pile in piles:
                res += pile // k + 1 * int(pile % k != 0)
            return res
        
        # 这里 minK 应该用 1 更好，但是 0 应该也没问题，打算先试试。
        minK, maxK = 0, max(piles)
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
https://leetcode.cn/submissions/detail/322435038/

18 / 119 个通过测试用例
状态：执行出错

执行出错信息：
ZeroDivisionError: integer division or modulo by zero
    res += pile // k + 1 * int(pile % k != 0)
Line 9 in calculate_time (Solution.py)
    if calculate_time(mid) < h:
Line 17 in minEatingSpeed (Solution.py)
    ret = Solution().minEatingSpeed(param_1, param_2)
Line 55 in _driver (Solution.py)
    _driver()
Line 66 in <module> (Solution.py)
最后执行的输入：
[312884470]
968709470
"""
