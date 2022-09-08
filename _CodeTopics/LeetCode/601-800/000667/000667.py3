class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        # 如果完全按升序或者降序排列，那么意味着只有一中不同的差值，也就是 1。
        # 如果把最小值和最大值放一块，那么这个差值一定是独一无二的。
        # 基于上述事实，先用当前最大挨着当前最小这种方式不断的排，最后剩下的升序就行。

        if k == 1:
            return list(range(1, n+1))
        
        left, right = 1, n
        round = 0
        res = []
        while k > 1:
            if not round:
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
            round ^= 1
            k -= 1
        
        if not round:
            remain = list(range(left, right+1))
        else:
            remain = list(range(right, left-1, -1))
        res.extend(remain)
        return res
        
"""
https://leetcode.cn/submissions/detail/360797300/

执行用时：
16 ms
, 在所有 Python 提交中击败了
82.35%
的用户
内存消耗：
14.2 MB
, 在所有 Python 提交中击败了
47.06%
的用户
通过测试用例：
70 / 70
"""
