class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        height = [0]
        for i in range(1, len(gain)+1):
            height.append(gain[i-1] + height[i-1])
        return max(height)
    
"""
https://leetcode-cn.com/submissions/detail/140627977/

80 / 80 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.9 MB
"""
