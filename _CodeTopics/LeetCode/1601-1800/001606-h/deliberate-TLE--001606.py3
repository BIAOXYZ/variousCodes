class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        # 第一反应是堆，但是先不打算细想，先写 trivial 的实现。
        # 这个时间复杂度是 O(n^2) 的，基本是超时预定。

        totalQueryPerServer = [0 for _ in range(k)]
        nextAvailableTime = [0 for _ in range(k)]
        n = len(arrival)
        for i in range(n):
            currTime, currLoad = arrival[i], load[i]
            if nextAvailableTime[i%k] <= currTime:
                totalQueryPerServer[i%k] += 1
                nextAvailableTime[i%k] = currTime + currLoad
            else:
                candidate = (i + 1) % k
                while nextAvailableTime[candidate] > currTime:
                    candidate = (candidate + 1) % k
                    if candidate == i%k:
                        break
                if candidate != i%k:
                    totalQueryPerServer[candidate] += 1
                    nextAvailableTime[candidate] = currTime + currLoad
        return [i for i in range(k) if totalQueryPerServer[i] == max(totalQueryPerServer)]
        
"""
https://leetcode-cn.com/submissions/detail/291778219/

105 / 108 个通过测试用例
状态：超出时间限制
"""
