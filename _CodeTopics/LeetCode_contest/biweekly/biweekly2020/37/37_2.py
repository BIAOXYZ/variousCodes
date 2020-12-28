import math
class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        
        def calculate_signal(x, y):
            total = 0
            for tower in towers:
                distance = math.sqrt((tower[0]-x)**2 + (tower[1]-y)**2)
                if distance <= radius:
                    total += int(tower[2] / (1+distance))
            return total
        
        maxX, maxY = towers[0][0], towers[0][1]
        minX, minY = towers[0][0], towers[0][1]
        for tower in towers:
            maxX, maxY = max(maxX, tower[0]), max(maxY, tower[1])
            minX, minY = min(minX, tower[0]), min(minY, tower[1])
        
        totalSignal = calculate_signal(towers[0][0], towers[0][1])
        res = [towers[0][0], towers[0][1]]
        for x in range(minX, maxX+1):
            for y in range(minY, maxY+1):
                tmp = calculate_signal(x,y)
                if totalSignal < tmp:
                    totalSignal = tmp
                    res = [x,y]
                elif totalSignal == tmp:
                    if x < res[0]:
                        res = [x,y]
                    elif x == res[0]:
                        if y < res[1]:
                            res = [x, y]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/116509110/

94 / 94 个通过测试用例
状态：通过
执行用时: 988 ms
内存消耗: 13.1 MB
"""
