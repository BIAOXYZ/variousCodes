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
        
        # 猜测前一个超时用例是因为最后每次又是求min，又是对list做remove。所以这里直接先倒着排序。
        # 然后最后那段逻辑，可以每次直接贴最后一个元素（也就是pop()出来的元素，所以正好一次做了）。
        for vals in dic.values():
            vals.sort(reverse=True)

        res = []
        for i in range(length):
            num = fa[i]
            res.append(dic[num].pop())
        return "".join(res)
        
"""
https://leetcode-cn.com/submissions/detail/137477422/

36 / 36 个通过测试用例
状态：通过
执行用时: 624 ms
内存消耗: 52 MB

执行用时：624 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：52 MB, 在所有 Python 提交中击败了60.00%的用户
"""
"""
哎呀，不小心混了个百分之百，不容易。。。
"""
