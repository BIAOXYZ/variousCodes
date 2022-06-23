class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n, m1, m2 = len(s), len(words), len(words[0])
        m = m1 * m2
        ctr = Counter(words)
        dic = {}
        for i in range(n - m2 + 1):
            dic[i] = '' if s[i:i+m2] not in ctr else s[i:i+m2]
        
        def make_initial_window(pos):
            wd = Counter()
            for i in range(pos, m, m2):
                if dic[i]:
                    wd[dic[i]] += 1
            return wd

        starts = list(range(m2))
        res = []
        for start in starts:
            for i in range(start, n - m + 1, m2):
                if i == start:
                    # 这里不能直接减，不然负数个数减不出来。。。
                    # diff = make_initial_window(i) - ctr
                    diff = make_initial_window(i)
                    diff.subtract(ctr)
                    for k in list(diff.keys()):
                        if diff[k] == 0:
                            diff.pop(k)
                else:
                    deleted_key = dic[i-m2]
                    added_key = dic[i+m-m2]
                    if deleted_key:
                        diff[deleted_key] -= 1
                        if diff[deleted_key] == 0:
                            diff.pop(deleted_key)
                    if added_key:
                        diff[added_key] += 1
                        if diff[added_key] == 0:
                            diff.pop(added_key)
                if not diff:
                    res.append(i)
        return res
        
"""
https://leetcode.cn/submissions/detail/328575642/

执行用时：
76 ms
, 在所有 Python3 提交中击败了
87.83%
的用户
内存消耗：
16.5 MB
, 在所有 Python3 提交中击败了
5.02%
的用户
通过测试用例：
177 / 177
"""
