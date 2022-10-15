class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        MOD = 10**9 + 7
        powers = []
        e = 0
        while n > 0:
            if n & 1 == 1:
                powers.append(2**e)
            n >>= 1
            e += 1
        ## print powers
        
        length = len(powers)
        prefixMul = [1] * length
        for i in range(length):
            if i == 0:
                prefixMul[i] = powers[i]
            else:
                prefixMul[i] = prefixMul[i-1] * powers[i]
        ## print prefixMul
        
        res = []
        for left, right in queries:
            curr = (prefixMul[right] / prefixMul[left] * powers[left]) % MOD
            res.append(curr)
        return res
    
"""
https://leetcode.cn/submissions/detail/373353299/

69 / 69 个通过测试用例
状态：通过
执行用时: 212 ms
内存消耗: 44.6 MB
"""
