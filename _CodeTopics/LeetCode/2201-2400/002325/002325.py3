class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        dic = {}
        offset = 0
        for ch in key:
            if ch != ' ' and ch not in dic:
                dic[ch] = chr(ord('a') + offset)
                offset += 1
                if offset >= 26:
                    break
        print(dic)
        res = []
        for ch in message:
            res.append(dic[ch]) if ch != ' ' else res.append(ch)
        return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/398518458/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
93.56%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
74.26%
的用户
通过测试用例：
69 / 69
"""
