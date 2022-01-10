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
                        # q1.append((nextY, nextY)) 日哦！
                        q1.append((nextX, nextY))
                    else:
                        if [nextX, nextY] == target:
                            return True
            if len(visited) > maxNumOfCoorInArea:
                beEncircled1 = False
                break
            # print(visited) 
            # 日他大爷，这句导致了一个 OLE，艹！ 
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
                        # q2.append((nextY, nextY)) 日哦！
                        q2.append((nextX, nextY))
            if len(visited) > maxNumOfCoorInArea:
                beEncircled2 = False
                break
        return False if beEncircled2 else True
        
"""
https://leetcode-cn.com/submissions/detail/257145210/

6 / 30 个通过测试用例
状态：超出时间限制

最后执行的输入：
[[419893,55778],[273187,99758],[717892,450294],[708088,481024],[576581,281428],[673502,35618],[761127,941602],[440312,903165],[131489,887659],[519661,559196],[608811,675228],[425641,365937],[842754,531655],[316187,587598],[51561,991459],[238261,211117],[890595,369481],[771312,66857],[587706,917241],[914885,993538],[535163,832595],[883316,72605],[912184,621663],[480641,772098],[107524,375877],[358066,962396],[699514,573077],[116819,230013],[132087,677569],[449650,351319],[381660,571870],[807331,714948],[994573,242727],[351932,209342],[164084,113850],[567386,535080],[860094,341720],[990235,204291],[669917,386729],[685026,448826],[126212,108918],[631319,235095],[862574,388974],[617636,873035],[290456,331169],[178233,461994],[432643,537288],[957512,888044],[430899,473083]]
[803314,571961]
[69769,128238]
"""
