class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        """
        思路：第一眼的想法是维护如下的字典：
             {a:[....], b:[...],..., !a:[], !b:[]...}
             但是如果a和b相等，其实两个字符key后面的list是一样的。
             这么一想这题目基本就是并查集了。。。
        """

        """
        # 没有路径压缩的find
        def find(x, fa):
            if x == fa[x]:
                return x
            else:
                return find(fa[x], fa)
        """

        def findandcompress(x, fa):
            if x != fa[x]:
                fa[x] = findandcompress(fa[x], fa)
            return fa[x]

        def union(x, y, fa):
            x = findandcompress(x, fa)
            y = findandcompress(y, fa)
            if x == y:
                return
            else:
                if x < y:
                    fa[y] = x
                else:
                    fa[x] = y
        
        fa = {}
        for i in range(97, ord('z')+1, 1):
            fa[chr(i)] = chr(i)

        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3], fa)
        for eq in equations:
            if eq[1] == "!":
                if findandcompress(eq[0], fa) == findandcompress(eq[3], fa):
                    return False
        return True
        
"""
# https://leetcode-cn.com/submissions/detail/77349512/

181 / 181 个通过测试用例
状态：通过
执行用时：44 ms
内存消耗：13 MB
"""
