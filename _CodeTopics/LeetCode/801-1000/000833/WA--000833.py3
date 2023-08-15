class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        n = len(s)
        res_lis = []
        i = j = 0
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
最后执行的输入

"vmokgggqzp"
[3,5,1]
["kg","ggq","mo"]
["s","so","bfr"]
"""
