class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """

        # 看题目如果若干点能形成一个“环”，他们在“环”内的位置就可以随便换。
        # 而这个“环”，想了想其实就是并查集。

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
        
        length = len(s)
        fa = [i for i in range(length)]
        for pair in pairs:
            union(pair[0], pair[1])
        # 我发现即使没有路径压缩，这也是个好办法——一个 “让fa变成全部是并查集代表组成的list” 的好办法。
        fa = [find(x) for x in fa]

        dic = {}
        for i in range(length):
            num = fa[i]
            if dic.has_key(num):
                dic[num].append(s[i])
            else:
                dic[num] = [s[i]]

        res = []
        for i in range(length):
            num = fa[i]
            res.append(min(dic[num]))
            dic[num].remove(min(dic[num]))
        return "".join(res)
        
"""
https://leetcode-cn.com/submissions/detail/137476698/

35 / 36 个通过测试用例
状态：超出时间限制
"""
