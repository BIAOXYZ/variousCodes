class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:

        # 由于前面的写法还是超时了，看来只能是用四个哈希表来记录当前被照亮的：
        ## 行、列、正对角线、反对角线的数目。
        ## 行和列很好表示，两种对角线则需要一定的“编码”。
        ## 目前想法是用统一用对角线和第一行或最后一行的交点的坐标来“编码”该对角线。
        # 但是写的过程中发现有个方面不是很好处理：是取上面还是取下面？
        ## 最后决定两个点都取，超出范围无所谓，反正只要能准确表示是哪条对角线即可。
        ## 实际写的时候可以只取两个纵坐标即可（因为横坐标肯定一个是0，一个是n-1）。

        lampSet = set(map(tuple, lamps))
        directions = [
            [-1,-1],[-1,0,],[-1,1],
            [0,-1],[0,0,],[0,1],
            [1,-1],[1,0,],[1,1],
        ]
        
        ctr_illuminated_rows = {}
        ctr_illuminated_cols = {}
        ctr_illuminated_diagonal1 = {}
        ctr_illuminated_diagonal2 = {}
        bound = n - 1
        for x, y in lamps:
            ctr_illuminated_rows[x] = ctr_illuminated_rows.setdefault(x, 0) + 1
            ctr_illuminated_cols[y] = ctr_illuminated_cols.setdefault(y, 0) + 1
            # 完整的应该是下面这个，但是正如前面所说，0和n-1可以省去。
            # k1, k2 = (0, y+(-x), bound, y+(bound-x)), (0, y+x, bound, y-(bound-x))
            k1, k2 = (y-x, y+bound-x), (y+x, y-bound+x)
            ctr_illuminated_diagonal1[k1] = ctr_illuminated_diagonal1.setdefault(k1, 0) + 1
            ctr_illuminated_diagonal2[k2] = ctr_illuminated_diagonal2.setdefault(k2, 0) + 1

        def be_illuminated(coor):
            x, y = coor[0], coor[1]
            k1, k2 = (y-x, y+bound-x), (y+x, y-bound+x)
            if ctr_illuminated_rows.get(x, 0) > 0 or \
                ctr_illuminated_cols.get(y, 0) > 0 or \
                ctr_illuminated_diagonal1.get(k1, 0) > 0 or \
                ctr_illuminated_diagonal2.get(k2, 0) > 0:
                return 1 
            return 0
        
        def is_legal_coor(coor):
            x, y = coor[0], coor[1]
            return 0 <= x < n and 0 <= y < n
        
        def turn_off_lamps(coor):
            x, y = coor[0], coor[1]
            for deltaX, deltaY in directions:
                newX, newY = x + deltaX, y + deltaY
                k1, k2 = (newY-newX, newY+bound-newX), (newY+newX, newY-bound+newX)
                if is_legal_coor([newX, newY]) and (newX, newY) in lampSet:
                    lampSet.remove((newX, newY))
                    ctr_illuminated_rows[newX] -= 1
                    ctr_illuminated_cols[newY] -= 1
                    ctr_illuminated_diagonal1[k1] -= 1
                    ctr_illuminated_diagonal2[k2] -= 1
        
        res = []
        for query in queries:
            res.append(be_illuminated(query))
            turn_off_lamps(query)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/266061386/

42 / 45 个通过测试用例
状态：解答错误

输入：
6
[[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]]
[[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]
输出：
[1,1,1,1,1,1]
预期结果：
[1,0,1,1,0,1]
"""
