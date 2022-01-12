from collections import deque
class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:

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
            if (x, y) in visited:
                continue
            visited.add((x, y))
            # 想了想判断 visited 内元素个数的if语句还是放在紧跟着visited.add()之后比较好。
            # 但是下面那一处故意没有改，也就是其实放后面也不是不行。
            if len(visited) > maxNumOfCoorInArea:
                beEncircled1 = False
                break
            for deltaX, deltaY in moves:
                nextX, nextY = x + deltaX, y + deltaY
                if (nextX, nextY) in visited:
                    continue
                if is_legal(nextX, nextY) and (nextX, nextY) not in blockedSet:
                    if [nextX, nextY] == target:
                        return True
                    else:
                        if (nextX, nextY) not in visited:
                            q1.append((nextX, nextY))
        if beEncircled1:
            return False
        
        q2 = deque([tuple(target)])
        visited = set()
        beEncircled2 = True
        while q2:
            x, y = q2.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for deltaX, deltaY in moves:
                nextX, nextY = x + deltaX, y + deltaY
                if (nextX, nextY) in visited:
                    continue
                if is_legal(nextX, nextY) and (nextX, nextY) not in blockedSet:
                    if (nextX, nextY) not in visited:
                        q2.append((nextX, nextY))
            if len(visited) > maxNumOfCoorInArea:
                beEncircled2 = False
                break
        return False if beEncircled2 else True
        
"""
https://leetcode-cn.com/submissions/detail/257809107/

执行用时：472 ms, 在所有 Python3 提交中击败了32.00%的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了27.20%的用户
通过测试用例：
30 / 30
"""
