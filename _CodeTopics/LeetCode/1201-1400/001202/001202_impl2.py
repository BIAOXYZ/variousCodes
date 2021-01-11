class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """

        # 和（`001202_impl.py`）没啥区别，只是把union中的 x < y 变成 x > y。
        # 从而说明：在选等价关系的代表时，一般来说，用大还是小都行。。。

        def find_and_compress(x):
            if x != fa[x]:
                fa[x] = find_and_compress(fa[x])
            return fa[x]
        
        def union(x, y):
            x, y = find_and_compress(x), find_and_compress(y)
            if x > y:
                fa[y] = x
            else:
                fa[x] = y
        
        length = len(s)
        fa = [i for i in range(length)]
        for pair in pairs:
            union(pair[0], pair[1])
        # 我发现即使没有路径压缩，这也是个好办法——一个 “让fa变成全部是并查集代表组成的list” 的好办法。
        fa = [find_and_compress(x) for x in fa]

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
https://leetcode-cn.com/submissions/detail/137713552/

36 / 36 个通过测试用例
状态：通过
执行用时: 592 ms
内存消耗: 51.8 MB

执行用时：592 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：51.8 MB, 在所有 Python 提交中击败了60.00%的用户
"""
"""
哎呀，不小心又混了个百分之百，还是击败了刚才的自己（`001202.py`）。。。
"""
