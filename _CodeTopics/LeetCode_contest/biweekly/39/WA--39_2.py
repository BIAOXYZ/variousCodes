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
        for m in range(maxval):
            for n in range(m+1):
                tmp = a*m - b*n
                if tmp in forbidden or tmp < 0:
                    break
                if tmp == x:
                    res = min(res, m+n)
        if res == float('inf'):
            return -1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/123466688/

17 / 87 个通过测试用例
状态：解答错误

输入：
[18,13,3,9,8,14]
3
8
6
输出：
2
预期：
-1
"""
