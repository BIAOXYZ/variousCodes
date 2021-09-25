class Solution(object):
    def bicycleYard(self, position, terrain, obstacle):
        """
        :type position: List[int]
        :type terrain: List[List[int]]
        :type obstacle: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n, m = len(terrain), len(terrain[0])
        
        # 只要不是完全平坦的，那么随便自行车一直乱骑，总会碰到能减速的点，直到最后减速为0，
        ## 所以这里也不用考虑 visited 了。
        # 但是有可能是完全平坦的图，也就是到任何点都无消耗，那么此时整个图除了出发点position，其他都可以。
        
        # 奶奶的就这规模也超时，所以想了想还是得搞个字典缓存一下。。。
        ## 一旦加了这个缓存，对于完全平坦的地形，也不用单独考虑了，因为速度不会变的，总会全部遍历完。
        visitedState = set()
        res = set()
        def dfs(x, y, speed):
            if (x, y, speed) in visitedState:
                return
            else:
                visitedState.add((x, y, speed))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for d in directions:
                newx, newy = x + d[0], y + d[1]
                if 0 <= newx < n and 0 <= newy < m:
                    h1, h2, o2 = terrain[x][y], terrain[newx][newy], obstacle[newx][newy]
                    newspeed = speed + h1 - h2 - o2
                    if newspeed > 0:
                        # 上一个错误会不会是因为这里，之前这里and后面部分写的是 (newx, newy) != position
                        # 左边tuple，右边list，等于没生效。。。
                        if newspeed == 1 and [newx, newy] != position:
                            res.add((newx, newy))
                        dfs(newx, newy, newspeed)
        
        dfs(position[0], position[1], 1)
        res = map(lambda x:list(x), res)
        return sorted(list(res))
    
"""
https://leetcode-cn.com/contest/season/2021-fall/submissions/223072282/
"""
