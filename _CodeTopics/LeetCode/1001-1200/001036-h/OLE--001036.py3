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
            print(visited)
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
https://leetcode-cn.com/submissions/detail/257145006/

4 / 30 个通过测试用例
状态：超出输出限制

最后执行的输入：
[[887968,76029],[478040,100615],[413693,211521],[84037,225089],[516868,914974],[161225,96123],[320456,162051],[70328,776373],[642302,711843],[115275,37429],[499329,577780],[735068,364357],[345167,829298],[135661,972336],[61002,836637],[951394,543688],[412217,135798],[710786,140643],[753732,863686],[774842,591769],[993338,581144],[153690,512200],[705935,957690],[140374,898192],[103638,250560]]
[147020,428481]
[197254,373912]
"""
