class Solution(object):
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """

        dic = {}
        for rel in relation:
            if dic.has_key(rel[0]):
                dic[rel[0]].add(rel[1])
            else:
                dic[rel[0]] = set([rel[1]])

        res = 0
        stk = [[0]]
        while k > 0:
            nextRoundPeople = []
            for peopleList in stk:
                key = peopleList[-1]
                if not dic.has_key(key):
                    continue
                for nextPeople in dic[key]:
                    tmp = peopleList + [nextPeople]
                    if tmp not in nextRoundPeople:
                        nextRoundPeople.append(tmp)
            stk = nextRoundPeople
            k -= 1
        
        for elem in stk:
            if elem[-1] == n-1:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/191206098/

27 / 28 个通过测试用例
状态：超出时间限制

最后执行的输入：
10
[[8,9],[2,8],[8,1],[6,9],[6,7],[2,3],[4,6],[3,7],[7,0],[5,6],[1,2],[8,5],[8,7],[9,6],[1,7],[2,4],[4,5],[5,8],[2,0],[5,7],[7,3],[9,8],[1,9],[4,9],[9,7],[4,0],[6,4],[9,2],[6,1],[6,5],[6,8],[2,6],[4,7],[2,9],[9,0],[3,0],[1,3],[4,1],[6,2],[9,4],[6,3],[3,2],[3,5],[5,1],[1,6],[8,6],[5,9],[7,4],[7,6],[0,1],[2,1],[5,2],[1,4],[8,3],[1,8],[7,1],[0,5],[3,1],[8,2],[0,8],[0,7],[0,9],[0,4],[5,3],[4,3],[7,2],[5,0],[7,9],[6,0],[7,5],[1,0],[9,3],[3,4],[7,8],[9,1],[5,4],[3,8],[1,5],[3,6],[2,5],[0,3],[0,2],[9,5],[8,4],[8,0],[2,7],[3,9],[0,6],[4,2],[4,8]]
5
"""
