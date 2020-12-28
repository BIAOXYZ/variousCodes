class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        
        if not arr:
            return 0
        
        length = len(arr)
        arr.sort()
        partialLen = length / 20
        summation = sum(arr[i] for i in range(partialLen, length-partialLen))
        return (summation * 1.0) / (length-partialLen-1)
        
"""
https://leetcode-cn.com/submissions/detail/116496903/

2 / 50 个通过测试用例
状态：解答错误

输入：
[6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
输出：
4.64865
预期：
4.77778
"""
