class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        
        n = len(plants)
        left, right = 0, n-1
        total = 0
        currA, currB = capacityA, capacityB
        
        while left < right:
            if plants[left] <= currA:
                currA -= plants[left]
            else:
                currA = capacityA - plants[left]
                total += 1
            left += 1
            if plants[right] <= currB:
                currB -= plants[right]
            else:
                currB = capacityB - plants[right]
                total += 1
            right -= 1
        
        if left == right:
            if max(currA, currB) < plants[left]:
                total += 1
        return total
    
"""
https://leetcode-cn.com/submissions/detail/247653826/

57 / 57 个通过测试用例
状态：通过
执行用时: 92 ms
内存消耗: 21.8 MB
"""
