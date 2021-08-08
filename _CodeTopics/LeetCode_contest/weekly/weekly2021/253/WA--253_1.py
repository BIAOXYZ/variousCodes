class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        
        w = ''.join(words)
        return w.startswith(s)
    
"""
https://leetcode-cn.com/submissions/detail/204481025/

337 / 346 个通过测试用例
状态：解答错误

最后执行的输入：
输入：
"a"
["aa","aaaa","banana"]
输出：
true
预期：
false
"""
