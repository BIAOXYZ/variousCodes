class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:

        # 第一反应的想法是维护整个 n*n 的矩阵，一个格子如果没被照亮，其值为0；
        ## 如果被一盏灯影响，其值就为1；如果被两盏灯影响，其值就为2；依次类推。
        ## 每当灭灯时，把所有这盏灯能影响到的格子里的值都减一。
        ## 那么每次query就只是看当前格子的值是否大于0即可。
        ## 但是，由于 n 太大，无法维护这样一个状态矩阵。。。

        # 那么接下来的想法就是用一个哈希集合维护当前还亮着的灯。
        ## 每次查询都遍历这个集合，看有没有灯能照到。
        ## 更新的话就是查询点周围的格子里如果有灯，就从哈希集合里移除。
        ## 如果只是trivial地这么写大概率还是超时，因为是 O(n^2) 的复杂度，
        ## 按题目里的输入规模，得有 4 * 10^8 了，超过了 10^8。
        ## 不过还是先这么写一下，后面在考虑比如用更多的哈希表记录哪些行、列完全被照亮之类的优化。

        lampSet = set(map(tuple, lamps))
        directions = [
            [-1,-1],[-1,0,],[-1,1],
            [0,-1],[0,0,],[0,1],
            [1,-1],[1,0,],[1,1],
        ]
        
        def be_illuminated(coor):
            # 答案要1和0，不要True和False。。。
            x, y = coor[0], coor[1]
            for lamp in lampSet:
                if x == lamp[0] or y == lamp[1] or x - lamp[0] == y - lamp[1]:
                    return 1
            return 0
        
        def is_legal_coor(coor):
            x, y = coor[0], coor[1]
            return 0 <= x < n and 0 <= y < n
        
        def turn_off_lamps(coor):
            x, y = coor[0], coor[1]
            for deltaX, deltaY in directions:
                newX, newY = x + deltaX, y + deltaY
                # 其实想想，不用判断坐标是否合法，因为反正不合法就不可能在亮着的灯的集合里。。。
                if is_legal_coor([newX, newY]) and (newX, newY) in lampSet:
                    lampSet.remove((newX, newY))
        
        res = []
        for query in queries:
            res.append(be_illuminated(query))
            turn_off_lamps(query)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/265691736/

30 / 45 个通过测试用例
状态：解答错误

输入：
6
[[1,1]]
[[2,0],[1,0]]
输出：
[0,0]
预期结果：
[1,0]
"""
