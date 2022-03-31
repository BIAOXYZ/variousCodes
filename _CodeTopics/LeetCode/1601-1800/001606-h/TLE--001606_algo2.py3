from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        # trivial 实现的 O(n^2) 主要是每次查找下一个可用的服务器时的复杂度是 O(n) 的。
        ## 叠加外层 for 循环，所以就超时了。
        # 下面是按照官方思想实现的，一个当前可用的服务器，用 sortedcontainer；另外一个
        ## 是其他服务器下次可用的时间点。

        totalQueryPerServer = [0 for _ in range(k)]
        nextAvailableTimeAndServer = []
        heapq.heapify(nextAvailableTimeAndServer)
        currAvailableServer = SortedList(range(k))

        n = len(arrival)
        for i in range(n):
            currTime, currLoad = arrival[i], load[i]
            while nextAvailableTimeAndServer and nextAvailableTimeAndServer[0][0] <= currTime:
                timeSeverPair = heapq.heappop(nextAvailableTimeAndServer)
                currAvailableServer.add(timeSeverPair[1])
            if not currAvailableServer:
                continue
            else:
                ind = currAvailableServer.bisect_left(i%k)
                if ind == len(currAvailableServer):
                    ind = 0
                candidate = currAvailableServer[ind]
                totalQueryPerServer[candidate] += 1
                currAvailableServer.remove(candidate)
                heapq.heappush(nextAvailableTimeAndServer, [currTime + currLoad, candidate])
        return [i for i in range(k) if totalQueryPerServer[i] == max(totalQueryPerServer)]
        
"""
https://leetcode-cn.com/submissions/detail/292905848/

105 / 108 个通过测试用例
状态：超出时间限制
"""
"""
这题太TM坑爹了，这个就跟官方答案区别不大，但是还是超时。。。
"""
