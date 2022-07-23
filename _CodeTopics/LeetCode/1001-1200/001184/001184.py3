class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start == destination:
            return 0
        n = len(distance)
        incrLine = 0
        
        nextStation = (start + 1) % n
        incrLine += distance[start]
        while nextStation != destination:
            incrLine += distance[nextStation]
            nextStation = (nextStation + 1) % n
        return min(incrLine, sum(distance) - incrLine)
        
"""
https://leetcode.cn/submissions/detail/340822476/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
40.33%
的用户
内存消耗：
15.5 MB
, 在所有 Python3 提交中击败了
74.67%
的用户
通过测试用例：
37 / 37
"""
