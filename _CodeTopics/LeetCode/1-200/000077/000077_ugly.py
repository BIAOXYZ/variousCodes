class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        if k > n:
            return []
        
        # 所以不要用全局或者类似函数内全局的变量combination，而是用局部的。
        # 不过回头可以探索下，这里用全局的怎么写。
        # combination = []
        res = []

        # 感觉用“当前可用的数字集”（比如故意错的答案里的 canBeUsed）好像不是那么好写，
        # 因为假设当前已用数字为[1,2]，剩下的就是[3,4]。一回溯，变成了[3,4,2]。
        # 当然也可用list的insert方法把2插到最前面，但是实际调试的结果来看，还是不少问题。
        # 所以改成用“目前已经在list里的数字”，很像树或图做搜索时，记录当前节点的状态。
        def calculate_ith_number(i, currarr):
            if i == k:
                # 这里不用deepcopy还是不行。还是太丑陋了。。。
                res.append(copy.deepcopy(currarr))
                return
            bound = currarr[-1] if currarr else 0
            for num in range(bound+1, n+1):
                # combination.append(num)
                currarr.append(num)
                calculate_ith_number(i+1, currarr)
                # combination.pop()
                currarr.pop()
                # 这里最开始写了这句，导致每次就可用num里第一个被遍历下去了。。。
                # return

        calculate_ith_number(0, [])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/106499607/

27 / 27 个通过测试用例
状态：通过
执行用时: 532 ms
内存消耗: 16.9 MB
"""
"""
执行用时：532 ms, 在所有 Python 提交中击败了29.46%的用户
内存消耗：16.9 MB, 在所有 Python 提交中击败了49.06%的用户
"""
