class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 先用记忆化搜索

        memoDic = {1:0}
        def memorize_search(k):
            if memoDic.has_key(k):
                return memoDic[k]
            if k & 1 == 0:
                memoDic[k] = 1 + memorize_search(k/2)
            else:
                memoDic[k] = 1 + min(memorize_search(k+1), memorize_search(k-1))
            return memoDic[k]
        
        return memorize_search(n)
        
"""
https://leetcode-cn.com/submissions/detail/240065319/

执行用时：16 ms, 在所有 Python 提交中击败了80.49%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了7.32%的用户
通过测试用例：
47 / 47
"""
