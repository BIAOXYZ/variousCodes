class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        # 从 lower 开始，找到叠加过程中最大的那个，看和 upper 能差几个。
        # 其实就是用前缀和数组里的最大最小值来计算。
        
        n = len(differences)
        prefixSum = [differences[0]]
        for i in range(1, n):
            prefixSum.append(prefixSum[-1] + differences[i])
        maxNum, minNum = max(prefixSum), min(prefixSum)
        
        res = 0
        for i in range(lower, upper+1):
            if i + maxNum <= upper and i + minNum >= lower:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/261365714/

82 / 82 个通过测试用例
状态：通过
执行用时: 468 ms
内存消耗: 27.3 MB
"""
