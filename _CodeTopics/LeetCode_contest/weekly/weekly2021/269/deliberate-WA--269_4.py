class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        
        def find(x):
            if fa[x] == x:
                return fa[x]
            else:
                return find(fa[x])
        
        def union(x, y):
            x, y = find(x), find(y)
            if x < y:
                fa[y] = x
            else:
                fa[x] = y
        
        meetings.sort(key=lambda x:x[2])
        length = len(meetings)
        fa = [i for i in range(n)]
        union(0, firstPerson)
        
        currMeeting = meetings[0]
        currTime = currMeeting[2]
        currUnionSet = {currMeeting[0], currMeeting[1]}
        i = 0
        while i < length:
            if currTime == meetings[i][2]:
                currUnionSet.add(meetings[i][0])
                currUnionSet.add(meetings[i][1])
                if i + 1 < length:
                    i += 1
                    continue
            se = list(currUnionSet)
            tmpfa = [find(x) for x in se]
            if 0 in tmpfa:
                for j in range(len(se)-1):
                    union(se[j], se[j+1])
            currMeeting = meetings[i]
            currTime = currMeeting[2]
            currUnionSet = {currMeeting[0], currMeeting[1]}
            i += 1
        se = list(currUnionSet)
        tmpfa = [find(x) for x in se]
        if 0 in tmpfa:
            for j in range(len(se)-1):
                union(se[j], se[j+1])
        
        res = []
        for i in range(n):
            if find(i) == 0:
                res.append(i)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/243044979/

17 / 42 个通过测试用例
状态：解答错误

输入：
6
[[0,2,1],[1,3,1],[4,5,1]]
1
输出：
[0,1,2,3,4,5]
预期：
[0,1,2,3]
"""
