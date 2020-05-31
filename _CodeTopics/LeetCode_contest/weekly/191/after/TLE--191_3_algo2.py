class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        reachablelist = [0]
        changenum = 0

        while len(reachablelist) < n:
            for i in range(len(connections)):
                if connections[i][0] not in reachablelist and connections[i][1] in reachablelist:
                    reachablelist.append(connections[i][0])
                elif connections[i][0] in reachablelist and connections[i][1] not in reachablelist:
                    connections[i][0],connections[i][1] = connections[i][1],connections[i][0]
                    changenum += 1
                    reachablelist.append(connections[i][0])
                else:
                    pass
        return changenum

"""
# https://leetcode-cn.com/submissions/detail/75156963/

67 / 69 个通过测试用例
状态：超出时间限制
最后执行的输入：44667
               [[1,0],[2,1],[2,3],[4,0],[1,5],[6,2],[7,1],[6,8],[9,6],[7,10],[11,10],[2,12],[8,13],[14,1],[15,4],[16,2],[17,15],...
"""
