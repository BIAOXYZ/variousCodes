class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        
        length = len(path)
        coordinates = [[0,0]]
        for i in range(length):
            # newcoordinate = coordinates[-1]
            # 草，又是这个坑。这里得申请新的list，再赋值。
            newcoordinate = [0,0]
            newcoordinate[0], newcoordinate[1] = coordinates[-1][0], coordinates[-1][1]
            if path[i] == 'N':
                newcoordinate[1] += 1
            elif path[i] == 'S':
                newcoordinate[1] -= 1
            elif path[i] == 'E':
                newcoordinate[0] += 1
            else:
                newcoordinate[0] -= 1
            if newcoordinate in coordinates:
                return True
            else:
                coordinates.append(newcoordinate)
        return False
    
"""
https://leetcode-cn.com/submissions/detail/82610114/

76 / 76 个通过测试用例
	状态：通过
执行用时：16 ms
内存消耗：13.1 MB
"""
