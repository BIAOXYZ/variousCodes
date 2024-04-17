from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        ctr = Counter(changed)
        keys = list(ctr.keys())
        keys.sort()

        res = []
        for k in keys:
            while ctr[k] > 0:
                doubledKey = k * 2
                if doubledKey not in keys or ctr[doubledKey] == 0:
                    return []
                else:
                    ctr[k] -= 1
                    ctr[doubledKey] -= 1
                    res.append(k)
        return res
        
"""
https://leetcode.cn/problems/find-original-array-from-doubled-array/submissions/524662338?envType=daily-question&envId=2024-04-18

解答错误
173 / 179 个通过的测试用例

输入
changed =
[0]
输出
[0]
预期结果
[]
"""
