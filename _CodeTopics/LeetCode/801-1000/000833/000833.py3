class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        n = len(s)
        res_lis = []
        i = j = 0
        _, sources = zip(*(sorted(zip(indices, sources))))
        _, targets = zip(*(sorted(zip(indices, targets))))
        indices.sort()
        while i < n:
            if j == len(indices):
                res_lis.append(s[i:])
                break
            if i != indices[j]:
                res_lis.append(s[i])
                i += 1
            else:
                sourceLen = len(sources[j])
                if s[i:i+sourceLen] == sources[j]:
                    res_lis.append(targets[j])
                    i += sourceLen
                else:
                    res_lis.append(s[i])
                    i += 1
                j += 1
        return "".join(res_lis)
        
"""
https://leetcode.cn/problems/find-and-replace-in-string/submissions/456768508/

时间
详情
48ms
击败 40.24%使用 Python3 的用户
内存
详情
15.62mb
击败 95.12%使用 Python3 的用户
"""
