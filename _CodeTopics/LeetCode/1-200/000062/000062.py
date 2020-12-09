class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        # 首先参照`deliberate-TLE--000062.py`和`deliberate-WA-after-TLE--000062.py`，
        # 是不是“自顶向下”的记忆化搜索就一定过不去呢？不是的，一般搞个哈希表存储函数结果就行。
        # --> 实质上，上面那俩只是做到了搜索，并没有“记忆化”，所以会超时。
        """

        def memorize_search(m, n):
            k = (m, n)
            if dic.has_key(k):
                return dic[k]
            else:
                if m == 1 or n == 1:
                    dic[k] = 1
                else:
                    dic[k] = memorize_search(m-1, n) + memorize_search(m, n-1)
            return dic[k]
        
        dic = dict()
        memorize_search(m, n)
        return dic[(m,n)]
        
"""
https://leetcode-cn.com/submissions/detail/129746460/

62 / 62 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.5 MB

执行用时：20 ms, 在所有 Python 提交中击败了64.09%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了5.01%的用户
"""
