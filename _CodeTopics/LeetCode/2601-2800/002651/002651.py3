class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:

        return (arrivalTime + delayedTime) % 24
        
"""
https://leetcode.cn/problems/calculate-delayed-arrival-time/submissions/464092122/?envType=daily-question&envId=2023-09-08

时间
详情
44ms
击败 58.31%使用 Python3 的用户
内存
详情
15.41MB
击败 99.44%使用 Python3 的用户
"""
