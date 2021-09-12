class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        length = len(points)
        dic = {}
        for i in range(length-1):
            for j in range(i+1, length):
                squareDistance = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if squareDistance in dic:
                    dic[squareDistance].append([i,j])
                else:
                    dic[squareDistance] = [[i,j]]
        
        def has_at_least_one_common_point(l1, l2):
            if l1[0] in l2 or l1[1] in l2:
                return True
            return False
        
        res = 0
        for v in dic.values():
            tmplen = len(v)
            if tmplen < 2:
                continue
            for i in range(tmplen-1):
                for j in range(i+1, tmplen):
                    if has_at_least_one_common_point(v[i], v[j]):
                        res += 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/218506282/

32 / 32 个通过测试用例
状态：通过
执行用时: 1108 ms
内存消耗: 54.7 MB

执行用时：1108 ms, 在所有 Python 提交中击败了28.57%的用户
内存消耗：54.7 MB, 在所有 Python 提交中击败了7.14%的用户
"""
