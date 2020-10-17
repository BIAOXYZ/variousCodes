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
                if tower[2] >= distance:
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
https://leetcode-cn.com/submissions/detail/116506012/

86 / 94 个通过测试用例
状态：解答错误

输入：
[[32,36,27],[17,22,43],[8,11,41],[46,28,7],[22,4,35],[41,8,33],[32,29,4],[44,32,16],[33,20,16],[3,38,35],[17,47,23],[33,0,29],[29,19,6],[4,50,46],[19,47,6],[48,6,41],[20,26,35]]
4
输出：
[17,22]
预期：
[4,50]
"""
