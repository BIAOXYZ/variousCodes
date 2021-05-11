class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        # 类似前缀和，是不是应该叫前缀异或？

        prefixXor = [arr[0]]
        for i in range(1, len(arr)):
            prefixXor.append(prefixXor[-1] ^ arr[i])

        res = []
        for l, r in queries:
            # res.append(prefixXor[l-1] ^ prefixXor[r])
            # 用 prefixXor[l-1] 可能会搞出 -1 来，还不如用下面形式这种直接了当。
            res.append(prefixXor[l] ^ prefixXor[r] ^ arr[l])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/176610198/

42 / 42 个通过测试用例
状态：通过
执行用时: 356 ms
内存消耗: 27.6 MB

执行用时：356 ms, 在所有 Python 提交中击败了36.36%的用户
内存消耗：27.6 MB, 在所有 Python 提交中击败了81.82%的用户
"""
