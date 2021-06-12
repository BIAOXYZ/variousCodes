# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 典型的二分查找（但是其实是类似有重二分查找）
        
        left, right = 1, n
        res = n
        while left <= right:
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/186215268/

22 / 22 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了54.78%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了15.38%的用户
"""
