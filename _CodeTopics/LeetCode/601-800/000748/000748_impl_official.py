from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        # 官方答案。主要是为了记下 min() 函数竟然也可以带自定义的比较函数。
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)
        
"""
https://leetcode-cn.com/submissions/detail/247031047/

执行用时：132 ms, 在所有 Python 提交中击败了5.88%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了44.12%的用户
通过测试用例：
102 / 102
"""
