class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        # 前一个（`TLE--001765.py3`）之所以会超时就是因为：虽然也注意到了是多源BFS，
        # 但是实际上写的时候搞到一个for循环里了，浪费了很多步骤：
        # ——> 每一次都从某个水域出发，把整个图遍历了一遍。
        # ——> 而实际上是不需要的，只需要像官方答案的写法一样，每次每个水域都扩散，
        #     且都是仅扩散一层。
        # ——> 此外，官方答案的写法连 visited 都不用标记，直接就用 -1 来判断：
        #     如果不是 -1，这一次不能标记，因为之前肯定有某一轮已经像这样每次按最大值标记
        #     过了，不可能比这个值还大了。

        m, n = len(isWater), len(isWater[0])
        res = [[-1 for j in range(n)] for i in range(m)]
        waterAreas = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    waterAreas.append((i, j))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def is_legal_coor(x, y):
            return 0 <= x < m and 0 <= y < n

        visited = set()
        heightOfCurrLevel = 0
        q = waterAreas
        while q:
            nextLevel = []
            for x, y in q:
                if (x, y) not in visited:
                    visited.add((x, y))
                else:
                    continue
                if res[x][y] == -1:
                    res[x][y] = heightOfCurrLevel
                else:
                    res[x][y] = min(res[x][y], heightOfCurrLevel)
                for d in directions:
                    nextx, nexty = x + d[0], y + d[1]
                    # 这个还是有 q 里面会有重复的节点，虽然并不影响正确性，但是需要想想怎么改掉
                    if is_legal_coor(nextx, nexty) and (nextx, nexty) not in visited:
                        nextLevel.append((nextx, nexty))
            q.clear()
            if nextLevel:
                q = nextLevel[:]
                heightOfCurrLevel += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/263344090/

执行用时：2600 ms, 在所有 Python3 提交中击败了14.73%的用户
内存消耗：188.8 MB, 在所有 Python3 提交中击败了16.28%的用户
通过测试用例：
59 / 59
"""
