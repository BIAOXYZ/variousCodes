class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 这个题trivial的（自顶向下）记忆化搜索/递归都能过。。。但是还是写个带哈希表的真正的记忆化搜索吧。

        def memorize_search(n):
            if dic.has_key(n):
                return dic[n]
            else:
                dic[n] = memorize_search(n-1) + memorize_search(n-2)
            return dic[n]

        dic = {0:0, 1:1}
        return memorize_search(n)
        
"""
https://leetcode-cn.com/submissions/detail/135723994/

31 / 31 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了79.54%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.03%的用户
"""
