class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        reachablelist = [0]
        connectionsLeft = []
        changenum = 0

        while len(reachablelist) < n:
            for i in range(len(connections)):
                if connections[i][0] not in reachablelist and connections[i][1] in reachablelist:
                    reachablelist.append(connections[i][0])
                elif connections[i][0] in reachablelist and connections[i][1] not in reachablelist:
                    changenum += 1
                    reachablelist.append(connections[i][1])
                else:
                    connectionsLeft.append(connections[i])
            connections = connectionsLeft
            connectionsLeft = []
        return changenum

"""
# https://leetcode-cn.com/submissions/detail/75168704/

67 / 69 个通过测试用例
	状态：超出时间限制
最后执行的输入： 44667
                [[1,0],[2,1],[2,3],[4,0],[1,5],[6,2],[7,1],[6,8],[9,6],[7,10],[11,10],[2,12],[8,13],[14,1],[15,4],[16,2],[17,15],...
"""
"""
这个algo3其实是algo2的优化版本，每次把剩下的元素放到新list里，从而大大下轮的遍历缩短时间。
我就醉了，我在讨论区看到algo2的python3版本都能过。。。我这更优的algo3的python版本过不了。。。
"""
