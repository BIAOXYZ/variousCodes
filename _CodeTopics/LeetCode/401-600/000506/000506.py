class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        length = len(score)
        tmp = zip(score, range(length))
        tmp.sort(reverse=True)
        
        res = [0 for _ in range(length)]
        for i, tup in enumerate(tmp):
            ind = tup[1]
            rank = str(i + 1)
            res[ind] = rank

        for i, rank in enumerate(res):
            if rank == "1":
                res[i] = "Gold Medal"
            elif rank == "2":
                res[i] = "Silver Medal"
            elif rank == "3":
                res[i] = "Bronze Medal"
        return res
        
"""
https://leetcode-cn.com/submissions/detail/244377390/

执行用时：24 ms, 在所有 Python 提交中击败了84.55%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了49.59%的用户
通过测试用例：
17 / 17
"""
