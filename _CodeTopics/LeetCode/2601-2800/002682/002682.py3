from collections import Counter
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        ctr = Counter({i+1:0 for i in range(n)})
        ctr[1] = 1
        currFriend, multiple = 1, 1
        while max(ctr.values()) < 2:
            nextFriend = (currFriend + multiple*k) % n
            if nextFriend == 0:
                nextFriend = n
            ctr[nextFriend] += 1
            currFriend = nextFriend
            multiple += 1
        return sorted(friend for friend, val in ctr.items() if val == 0)
        
"""
https://leetcode.cn/problems/find-the-losers-of-the-circular-game/submissions/456800595/

时间
详情
64ms
击败 8.46%使用 Python3 的用户
内存
详情
15.70mb
击败 50.97%使用 Python3 的用户
"""
