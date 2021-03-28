class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """
        吐槽下：为什么这道题的输入输出注释和别的题目都不一样？。。。
        """
        """
        # 再次吐槽：这道题官方的后台程序没搞好，python语言连题目里的测试用例执行时都会报格式错。。。
        # 去了海外LeetCode也是一样的，坑。。。https://leetcode.com/problems/reverse-bits/
        # 本打算先用C++写，想想还是算了，找个一行的手动狗头提交一下： 
        # https://leetcode.com/problems/reverse-bits/discuss/54765/One-line-solution-in-Python-%3A)
        """
        return int(bin(n)[2:].zfill(32)[::-1], 2)
        
"""
https://leetcode-cn.com/submissions/detail/161088225/

600 / 600 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB

执行用时：16 ms, 在所有 Python 提交中击败了85.05%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了11.21%的用户
"""
