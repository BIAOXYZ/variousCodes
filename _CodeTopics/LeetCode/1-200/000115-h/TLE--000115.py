class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        # 最plain的方法是用回溯算法穷举 s 的所有长度和 t 相等的子序列，然后过程中计数。
        # 但是感觉这种方法应该会超时。毕竟指数级，输入长度又有 1000 左右。

        lens, lent = len(s), len(t)
        if lens < lent or (lens == lent and s != t):
            return 0
        
        res = [0]
        def backtrack_dfs(start, currStr, start2):
            # 偶然发现如果currStr在这里连接的话（而不是在回溯末尾的for循环里），
            # 其实后面可以省掉cut掉新加的字符或者pop出数组元素（如果是list的话）之类的操作。
            currStr += s[start]
            if len(currStr) == lent:
                if currStr == t:
                    res[0] += 1
                return
            if len(currStr) + lens - 1 - start < lent:
                return
            for nextStart in range(start+1, lens):
                if s[nextStart] == t[start2+1]:
                    backtrack_dfs(nextStart, currStr, start2+1)
        
        for i in range(lens-lent+1):
            if s[i] == t[0]:
                backtrack_dfs(i, "", 0)
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/156102320/

52 / 62 个通过测试用例
状态：超出时间限制

最后执行的输入：
"daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac"
"ceadbaa"
"""
