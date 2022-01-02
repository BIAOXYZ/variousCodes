class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        
        asteroids.sort()
        n = len(asteroids)
        pos = 0
        while pos < n:
            if mass >= asteroids[pos]:
                mass += asteroids[pos]
                pos += 1
            else:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/254169788/

66 / 66 个通过测试用例
状态：通过
执行用时: 168 ms
内存消耗: 21.9 MB
"""
