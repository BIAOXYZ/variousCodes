class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        n, m1, m2 = len(s), len(words), len(words[0])
        m = m1 * m2
        ctr = Counter(words)
        dic = {}
        for i in range(n - m + 1):
            dic[i] = '' if s[i:i+m2] not in ctr else s[i:i+m2]
        
        def make_initial_window(pos):
            ctr = Counter()
            for i in range(pos, m, m2):
                if dic[i]:
                    ctr[dic[i]] += 1
            return ctr

        starts = list(range(m2))
        res = []
        for start in starts:
            for i in range(start, n - m + 1, m2):
                if i == start:
                    diff = make_initial_window(i) - ctr
                else:
                    deleted_key = dic[i-m2]
                    added_key = dic[i+m-m2]
                    if deleted_key:
                        diff[deleted_key] -= 1
                    if added_key:
                        diff[added_key] += 1
                if not diff:
                    res.append(i)
        return res
