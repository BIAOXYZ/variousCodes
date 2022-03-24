class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        m, n = len(img), len(img[0])
        def is_legal_coor(coor):
            return 0 <= coor[0] < m and 0 <= coor[1] < n
        
        directions = [[dx, dy] for dx in range(-1, 2) for dy in range(-1, 2)]
        res = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                summ, quantity = 0, 0
                for dx, dy in directions:
                    if is_legal_coor([x+dx, y+dy]):
                        summ += img[x+dx][y+dy]
                        quantity += 1
                res[x][y] = summ // quantity
        return res
        
"""
https://leetcode-cn.com/submissions/detail/288535735/

执行用时：428 ms, 在所有 Python3 提交中击败了13.02%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了56.80%的用户
通过测试用例：
203 / 203
"""
