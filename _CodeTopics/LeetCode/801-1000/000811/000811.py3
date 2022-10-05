import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        ddic = collections.defaultdict(int)
        for domain in cpdomains:
            n = len(domain)
            whiteSpaceIndex = domain.index(' ')
            frequency = int(domain[:whiteSpaceIndex])
            fullName = domain[whiteSpaceIndex+1:]
            ddic[fullName] += frequency
            for i in range(n-1, -1, -1):
                if domain[i] == '.':
                    key = domain[i+1:]
                    ddic[key] += frequency
        return [str(v) + ' ' + k for k, v in ddic.items()]
        
"""
https://leetcode.cn/submissions/detail/370013895/

执行用时：
64 ms
, 在所有 Python3 提交中击败了
5.24%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
75.24%
的用户
通过测试用例：
52 / 52
"""
