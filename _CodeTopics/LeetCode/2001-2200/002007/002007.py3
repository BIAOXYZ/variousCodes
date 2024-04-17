from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
                
        ctr = Counter(changed)
        res = []
        if 0 in ctr and ctr[0] % 2 == 1:
            return []
        else:
            res.extend([0 for _ in range(ctr[0]//2)])
            del ctr[0]

        keys = list(ctr.keys())
        keys.sort()
        for k in keys:
            if ctr[k] > 0:
                doubledKey = k * 2
                if doubledKey not in ctr or ctr[doubledKey] < ctr[k]:
                    return []
                else:
                    res.extend([k] * ctr[k])
                    ctr[doubledKey] -= ctr[k]
        return res
        
"""
https://leetcode.cn/problems/find-original-array-from-doubled-array/submissions/524664390?envType=daily-question&envId=2024-04-18

通过
零知识证明
提交于 2024.04.18 01:51

执行用时分布
199
ms
击败
88.03%
使用 Python3 的用户
消耗内存分布
32.57
MB
击败
80.34%
使用 Python3 的用户
"""
