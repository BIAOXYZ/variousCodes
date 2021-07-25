class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        
        m, n = len(students), len(students[0])
        def cal_match_score(stu, men):
            res = 0
            for i in range(n):
                if stu[i] == men[i]:
                    res += 1
            return res
        
        maxScore = [0]
        def back_track(currMatch, availMen):
            if not availMen:
                total = 0
                for i in currMatch:
                    total += cal_match_score(students[i], mentors[currMatch[i]])
                maxScore[0] = max(maxScore[0], total)
                return
            for men in availMen:
                currMatch.append(men)
                ind = availMen.index(men)
                availMen.remove(men)
                back_track(currMatch, availMen)
                currMatch.pop()
                availMen.insert(ind, men)
        
        back_track([], range(m))
        return maxScore[0]
    
"""
https://leetcode-cn.com/submissions/detail/199536146/

86 / 86 个通过测试用例
状态：通过
执行用时: 3044 ms
内存消耗: 13.2 MB
"""
