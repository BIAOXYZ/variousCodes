from collections import deque
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        # 参考官方答案的“包围圈”方法。

        EDGE_LENGTH = 10**6
        n = len(blocked)
        blockedSet = set([tuple(block) for block in blocked])
        maxNumOfCoorInArea = n * (n-1) // 2
        moves = [[0,1],[0,-1],[1,0],[-1,0]]

        def is_legal(x, y):
            return 0 <= x < EDGE_LENGTH - 1 and 0 <= y < EDGE_LENGTH - 1
        
        q1 = deque([tuple(source)])
        visited = set()
        beEncircled1 = True
        while q1:
            x, y = q1.popleft()
            visited.add((x, y))
            for deltaX, deltaY in moves:
                nextX, nextY = x + deltaX, y + deltaY
                if (nextX, nextY) in visited:
                    continue
                if is_legal(nextX, nextY):
                    if (nextX, nextY) not in blockedSet:
                        q1.append((nextY, nextY))
                    else:
                        if [nextX, nextY] == target:
                            return True
            if len(visited) > maxNumOfCoorInArea:
                beEncircled1 = False
                break
        if beEncircled1:
            return False
        
        q2 = deque([tuple(target)])
        visited = set()
        beEncircled2 = True
        while q2:
            x, y = q2.popleft()
            visited.add((x, y))
            for deltaX, deltaY in moves:
                nextX, nextY = x + deltaX, y + deltaY
                if (nextX, nextY) in visited:
                    continue
                if is_legal(nextX, nextY):
                    if (nextX, nextY) not in blockedSet:
                        q2.append((nextY, nextY))
            if len(visited) > maxNumOfCoorInArea:
                beEncircled2 = False
                break
        return False if beEncircled2 else True
        
"""
https://leetcode-cn.com/submissions/detail/257144456/

2 / 30 个通过测试用例
状态：超出时间限制

最后执行的输入：
[[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]]
[655988,180910]
[267728,840949]
"""
