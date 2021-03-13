from functools import lru_cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        length = len(s)

        # 用python3的functools搞记忆化搜索简直爽死。。。
        # 另外，之前见到的都是 @lru_cache(None) 和 @lru_cache()，
        # 但这次官方答案里是用 @cache，不知道有啥区别。。。
        @lru_cache()
        def is_palindrome(start, end):
            if end == start:
                return True
            elif end - start == 1:
                return s[start] == s[end]
            else:
                return s[start] == s[end] and is_palindrome(start+1, end-1)

        # 用类似官方答案里的回溯算法处理，写完对比了下，答案写的还是更简单啊。
        def backtrack_dfs(currArr, start):
            if start == length:
                res.append(currArr[:])
                return
            for end in range(start+1, length+1):
                currStr = s[start:end]
                if is_palindrome(start, end-1):
                    currArr.append(currStr)
                    backtrack_dfs(currArr, end)
                    currArr.pop()
        
        res = []
        backtrack_dfs([], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/154807513/

32 / 32 个通过测试用例
状态：通过
执行用时: 168 ms
内存消耗: 31 MB

执行用时：168 ms, 在所有 Python3 提交中击败了34.61%的用户
内存消耗：31 MB, 在所有 Python3 提交中击败了42.16%的用户
"""
