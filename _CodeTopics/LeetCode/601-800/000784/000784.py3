class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        n = len(s)
        alphabeta = [chr(i) for i in range(ord('a'), ord('z')+1)]
        alphabetaSet = set(alphabeta)
        res = set()
        
        def backtrack(currPos, currArr):
            if currPos == n:
                res.add(''.join(currArr))
                return
            if s[currPos].isdigit():
                currArr.append(s[currPos])
                backtrack(currPos+1, currArr)
                currArr.pop()
            else:
                for ch in [s[currPos].lower(), s[currPos].upper()]:
                    currArr.append(ch)
                    backtrack(currPos+1, currArr)
                    currArr.pop()
        
        backtrack(0, [])
        return list(res)
        
"""
https://leetcode.cn/submissions/detail/377658289/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
58.90%
的用户
内存消耗：
16.5 MB
, 在所有 Python3 提交中击败了
15.46%
的用户
通过测试用例：
63 / 63
"""
