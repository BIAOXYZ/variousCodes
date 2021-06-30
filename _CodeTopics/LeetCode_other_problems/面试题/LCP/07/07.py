class Solution(object):
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """

        # 其实不需要每次把整个完整的传递线路都贴到存储空间，只贴最后一个元素即可。

        dic = {}
        for rel in relation:
            if dic.has_key(rel[0]):
                dic[rel[0]].add(rel[1])
            else:
                dic[rel[0]] = set([rel[1]])

        res = 0
        stk = [0]
        while k > 0:
            nextRoundPeople = []
            for lastPeople in stk:
                if not dic.has_key(lastPeople):
                    continue
                else:
                    nextRoundPeople.extend(list(dic[lastPeople]))
            stk = nextRoundPeople
            k -= 1
        
        for elem in stk:
            if elem == n-1:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/191206269/

28 / 28 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.4 MB

执行用时：24 ms, 在所有 Python 提交中击败了50.00%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了15.63%的用户
"""
