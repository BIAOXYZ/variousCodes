class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        MOD = 10**9 + 7
        
        @cache
        def calculate_apples(x1, y1, x2, y2):
            return sum([1 for x in range(x1, x2+1) for y in range(y1, y2+1) if pizza[x][y] == 'A'])

        memoDic = {}
        def memorize_search(leftupX, leftupY, rightdownX, rightdownY, n_persons):
            key = (leftupX, leftupY, rightdownX, rightdownY, n_persons)
            if key in memoDic:
                return memoDic[key]
            
            n_apples = calculate_apples(leftupX, leftupY, rightdownX, rightdownY)
            if n_apples < n_persons:
                memoDic[key] = 0
                return 0
            if n_persons == 1:
                memoDic[key] = 1
                return 1
            
            memoDic[key] = 0
            for incr in range(1, rightdownX - leftupX + 1):
                nextX = leftupX + incr
                will_use_apples = calculate_apples(leftupX, leftupY, nextX-1, rightdownY)
                if will_use_apples == 0:
                    continue
                memoDic[key] += memorize_search(nextX, leftupY, rightdownX, rightdownY, n_persons-1)
            for incr in range(1, rightdownY - leftupY + 1):
                nextY = leftupY + incr
                will_use_apples = calculate_apples(leftupX, leftupY, rightdownX, nextY-1)
                if will_use_apples == 0:
                    continue
                memoDic[key] += memorize_search(leftupX, nextY, rightdownX, rightdownY, n_persons-1)
            return memoDic[key]
        
        rows, cols = len(pizza), len(pizza[0])
        return memorize_search(0, 0, rows-1, cols-1, k) % MOD
        
"""
https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/submissions/457284389/

时间
详情
4128ms
击败 5.75%使用 Python3 的用户
内存
详情
33.83mb
击败 5.75%使用 Python3 的用户
"""
