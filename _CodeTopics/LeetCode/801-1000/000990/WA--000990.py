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
        def find(x, fa):
            if x == fa[x]:
                return x
            else:
                return find(fa[x], fa)
 
        def findandcompress(x, fa):
            if x != fa[x]:
                fa[x] = findandcompress(fa[x], fa)
            return fa[x]

        def union(x, y, fa):
            x = find(x, fa)
            y = find(y, fa)
            if x == y:
                return
            else:
                if x < y:
                    fa[y] = x
                else:
                    fa[x] = y
        """

        def find_for_this_problem(x, fa):
            # 这个主要是为了处理根据 !b 的father是c找到c，但是c又不在并查集里的情况：
            # （比如 ["a==b","b!=c","c==a"]）
            if not fa.has_key(x):
                return x
            if x != fa[x]:
                fa[x] = find_for_this_problem(fa[x], fa)
            return fa[x]

        djs = {}
        negset = set()
        for eq in equations:
            if eq[0] == eq[3] and eq[1] == "=":
                continue
            elif eq[0] == eq[3] and eq[1] == "!":
                return False
            elif eq[0] != eq[3] and eq[1] == "=":
                larger =  max(eq[0], eq[3])
                smaller =  min(eq[0], eq[3])
                if not djs.has_key(larger):
                    djs[larger] = smaller
                else:
                    djs[larger] = min(smaller, djs[larger])
                if not djs.has_key(smaller):
                    djs[smaller] = smaller
                else:
                    pass
                ##print "djs changed in 1 is: ", djs
            else:
                negkey0 = "!" + eq[0]
                negkey3 = "!" + eq[3]
                if not djs.has_key(negkey0):
                    djs[negkey0] = eq[3]
                else:
                    djs[negkey0] = min(eq[3], djs[negkey0])
                if not djs.has_key(negkey3):
                    djs[negkey3] = eq[0]
                else:
                    djs[negkey3] = min(eq[0], djs[negkey3])
                ##print "djs changed in 2 is: ", djs
                negset.add(negkey0)
                negset.add(negkey3)
                # 这块是希望有些时候某个不等式一过来就能快速结束。但是也有可能不能，
                # 所以最后用for循环再来一遍。
                if djs.has_key(eq[0]) and find_for_this_problem(negkey0, djs) == find_for_this_problem(eq[0], djs):
                    return False
                if djs.has_key(eq[3]) and find_for_this_problem(negkey3, djs) == find_for_this_problem(eq[3], djs):
                    return False
        
        for negkey in negset:
            if djs.has_key(negkey[1]) and find_for_this_problem(negkey, djs) == find_for_this_problem(negkey[1], djs):
                return False
        return True

"""
# https://leetcode-cn.com/submissions/detail/77304350/

165 / 181 个通过测试用例
状态：解答错误

输入：["b!=f","c!=e","f==f","d==f","b==f","a==f"]
输出：true
预期：false
"""
