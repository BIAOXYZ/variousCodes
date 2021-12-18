from collections import defaultdict
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        trustDic, beTrustedDic = defaultdict(set), defaultdict(set)
        for person1, person2 in trust:
            trustDic[person1].add(person2)
            beTrustedDic[person2].add(person1)

        everybodyTrust = set()
        trustNobody = set()
        for i in range(1, n+1):
            if trustDic[i] == set():
                trustNobody.add(i)
            if len(beTrustedDic[i]) == n - 1:
                everybodyTrust.add(i)

        se = everybodyTrust & trustNobody
        return -1 if len(se) != 1 else se.pop()
        
"""
https://leetcode-cn.com/submissions/detail/249804813/

执行用时：84 ms, 在所有 Python 提交中击败了36.89%的用户
内存消耗：17.7 MB, 在所有 Python 提交中击败了5.74%的用户
通过测试用例：
92 / 92
"""
