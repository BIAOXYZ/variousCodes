class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        # 贪心思想：如果某一个字符串 s 的子序列符合条件，那么 s 本身更加符合条件。
        # strs 里所有的字符串应该是长度从长到短。

        strs.sort(key = lambda x : len(x), reverse=True)
        n = len(strs)
        
        def is_subsequence(s1, s2):
            len1, len2 = len(s1), len(s2)
            if len1 > len2 or (len1 == len2 and s1 != s2):
                return False
            else:
                ptr1 = ptr2 = 0
                while ptr1 < len1:
                    ch = s1[ptr1]
                    while ptr2 < len2 and s2[ptr2] != ch:
                        ptr2 += 1
                    if ptr2 < len2:
                        ptr1 += 1
                        ptr2 += 1
                    else:
                        return False
            return True
        
        for i in range(n):
            flag = True
            for j in range(n):
                if j == i:
                    continue
                if is_subsequence(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1
        
"""
https://leetcode.cn/submissions/detail/329963360/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
93.03%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
57.71%
的用户
通过测试用例：
98 / 98
"""
