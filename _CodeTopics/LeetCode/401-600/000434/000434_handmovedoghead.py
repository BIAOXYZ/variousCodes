class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 手动狗头题
        # 原来的写法： return len(s.split(' ')) if s.count(' ') != len(s) else 0 
        ## 里，字符串的 split() 方法里的空格还画蛇添足了。。。
        return len(s.split()) if s.count(' ') != len(s) else 0
        
"""
https://leetcode-cn.com/submissions/detail/226337479/

27 / 27 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB

执行用时：16 ms, 在所有 Python 提交中击败了64.23%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了49.63%的用户
"""
