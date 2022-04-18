class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        return sorted(range(1,n+1), key = lambda x : str(x))
        
"""
https://leetcode-cn.com/submissions/detail/302148562/

执行用时：
60 ms
, 在所有 Python3 提交中击败了
74.01%
的用户
内存消耗：
21.5 MB
, 在所有 Python3 提交中击败了
15.24%
的用户
通过测试用例：
26 / 26
"""
