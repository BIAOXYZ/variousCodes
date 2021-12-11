import bisect
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        length = len(times)
        self.candidatePerTime = [-1] * length
        currCandidate, currMaxBallot = -1, 0
        dic = {}
        for i in range(length):
            dic[persons[i]] = dic.setdefault(persons[i], 0) + 1
            if dic[persons[i]] >= currMaxBallot:
                currCandidate = persons[i]
                currMaxBallot = max(currMaxBallot, dic[persons[i]])
            self.candidatePerTime[i] = currCandidate
        ##print times
        ##print self.candidatePerTime

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        ind = bisect.bisect(self.times, t)
        return self.candidatePerTime[ind-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

"""
https://leetcode-cn.com/submissions/detail/247428258/

执行用时：1408 ms, 在所有 Python 提交中击败了71.43%的用户
内存消耗：18.6 MB, 在所有 Python 提交中击败了85.71%的用户
通过测试用例：
97 / 97
"""
