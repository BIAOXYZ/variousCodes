from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:

        stk = deque([])
        curr = ''
        for ch in path:
            if ch == '/':
                if not curr:
                    curr = '/'
                elif curr[-1] == '/':
                    continue
                else:
                    stk.append(curr)
                    curr = '/'
            else:
                curr += ch
        if curr != '/':
            stk.append(curr)
        
        res = []
        for subpath in stk:
            if subpath == '/.':
                continue
            elif subpath == '/..':
                if res:
                    res.pop()
            else:
                res.append(subpath)
        return ''.join(res) if res else '/'
        
"""
https://leetcode-cn.com/submissions/detail/255412342/

执行用时：36 ms, 在所有 Python3 提交中击败了53.79%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了6.36%的用户
通过测试用例：
256 / 256
"""
