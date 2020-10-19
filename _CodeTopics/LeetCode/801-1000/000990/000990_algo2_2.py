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

        def findandcompress(x):
            if x != fa[x]:
                fa[x] = findandcompress(fa[x])
            return fa[x]

        def union(x, y):
            x = findandcompress(x)
            y = findandcompress(y)
            if x == y:
                return
            else:
                fa[x] = y
        
        # 这种可以让find和union不用输fa这个参数。但是注意此时fa必须叫这个名字，不能叫fa1之类的。
        fa = {}
        for i in range(97, ord('z')+1, 1):
            fa[chr(i)] = chr(i)

        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])
        for eq in equations:
            if eq[1] == "!":
                if findandcompress(eq[0]) == findandcompress(eq[3]):
                    return False
        return True
        
"""
# https://leetcode-cn.com/submissions/detail/77374611/

181 / 181 个通过测试用例
状态：通过
执行用时：36 ms
内存消耗：13.2 MB
"""
