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
        # return [i for i in range(k) if totalQueryPerServer[i] == max(totalQueryPerServer)]
        # 又对比了下官方答案，感觉可能出问题的就是上面那行，果然。。。换成下面两行就过了。Python这优化也太
        # 差了吧。。。解释器不知道把 max(totalQueryPerServer) 存一下吗？！。。。
        maxVal = max(totalQueryPerServer)
        return [i for i in range(k) if totalQueryPerServer[i] == maxVal]
        
"""
https://leetcode-cn.com/submissions/detail/292906372/

执行用时：1280 ms, 在所有 Python3 提交中击败了44.15%的用户
内存消耗：36.1 MB, 在所有 Python3 提交中击败了6.46%的用户
通过测试用例：
108 / 108
"""
"""
注：对比一下 `TLE--001606_algo2.py3`，又学到了。直接参看这个提交最后 return 语句吧。
    Python 这解释器也太不给力了。。。这点优化也不自动搞- -
"""
