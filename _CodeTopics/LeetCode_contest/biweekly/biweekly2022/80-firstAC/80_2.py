class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        
        n, m = len(spells), len(potions)
        potions.sort()
        
        res = []
        for i in range(n):
            cur = spells[i]
            left, right = 0, m-1
            ind = -1
            while left <= right:
                mid = left + (right - left) / 2
                if cur * potions[mid] < success:
                    left = mid + 1
                else:
                    ind = mid
                    right = mid - 1
            if ind != -1:
                res.append(m - ind)
            else:
                res.append(0)
        return res
    
"""
https://leetcode.cn/submissions/detail/324218421/

56 / 56 个通过测试用例
状态：通过
执行用时: 720 ms
内存消耗: 35.9 MB
"""
