class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ddic = defaultdict(int)
        se = set()
        for winner, loser in matches:
            ddic[loser] += 1
            se.add(winner)
            se.add(loser)
        
        res = [[],[]]
        for player in se:
            if ddic[player] == 0:
                res[0].append(player)
            elif ddic[player] == 1:
                res[1].append(player)
        res[0].sort()
        res[1].sort()
        return res
    
"""
https://leetcode-cn.com/submissions/detail/293982493/

127 / 127 个通过测试用例
状态：通过
执行用时: 312 ms
内存消耗: 57.6 MB
"""
