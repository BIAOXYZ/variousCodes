class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        # 这次用（自顶向下的）记忆化搜索，把所有子串是不是回文先预处理好。
        # 我发现记忆化搜索还是更模板化一些，有时候复杂的情况 dp 没有 memorize_search 好写。

        length = len(s)

        dic = {}
        def is_palindrome(start, end):
            key = tuple([start, end])
            if dic.has_key(key):
                return dic[key]
            else:
                if end == start:
                    dic[key] = True
                elif end - start == 1:
                    dic[key] = s[start] == s[end]
                else:
                    dic[key] = s[start] == s[end] and is_palindrome(start+1, end-1)
            return dic[key]

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
https://leetcode-cn.com/submissions/detail/154802988/

32 / 32 个通过测试用例
状态：通过
执行用时: 176 ms
内存消耗: 48.2 MB

执行用时：176 ms, 在所有 Python 提交中击败了46.46%的用户
内存消耗：48.2 MB, 在所有 Python 提交中击败了51.75%的用户
"""
