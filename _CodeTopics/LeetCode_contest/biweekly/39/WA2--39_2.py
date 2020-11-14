class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        
        # 动态规划应该也可以，但是想了想还是没想完全细节，不过反而是在想dp的过程
        # 中想到解不定方程的数学方法：等价于求 am - bn = x 的解中，使得
        # m + n 值最小，且 n <= m 的解。
        
        maxval = 2000
        res = float('inf')
        
        secondbreak = False
        for m in range(maxval):
            for n in range(m+1):
                tmp = a*m - b*n
                if tmp in forbidden:
                    secondbreak = True
                    break
                if tmp == x:
                    res = min(res, m+n)
                if tmp < 0:
                    break
            if secondbreak:
                break
        if res == float('inf'):
            return -1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/123470000/

22 / 87 个通过测试用例

提交时间：38 分钟前
输入：
[5,2,10,12,18]
8
6
16
输出：
-1
预期：
2
"""
