class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        dic = {}
        for time in times:
            if dic.has_key(time[0]):
                dic[time[0]].append(time)
            else:
                dic[time[0]] = [time]

        visied = {k:0}
        visiedTuple = set() 
        def dfs_network(u):
            if not dic.has_key(u):
                return
            for time in dic[u]:
                if tuple(time) in visiedTuple:
                    continue
                visiedTuple.add(tuple(time))
                # time[0] 就不用额外赋值了，它就是 u
                v, w = time[1], time[2]
                if visied.has_key(v):
                    visied[v] = min(visied[u] + w, visied[v])
                else:
                    visied[v] = visied[u] + w
                dfs_network(time[1])
        
        dfs_network(k)
        if len(visied) < n:
            return -1
        return max(visied.values())
        
"""
https://leetcode-cn.com/submissions/detail/202191795/

19 / 52 个通过测试用例
状态：解答错误

最后执行的输入：
[[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]]
5
1
输出：
98
预期结果：
69
"""
