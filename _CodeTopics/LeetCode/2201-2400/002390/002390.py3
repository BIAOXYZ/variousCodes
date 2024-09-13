class Solution:
    def removeStars(self, s: str) -> str:

        n_undeleted = 0
        res_lis = []
        
        # 反向遍历字符串，有一个星号，就说明最近的一个非星号字符需要删除。
        for ch in reversed(s):
            if ch == '*':
                n_undeleted += 1
            else:
                if n_undeleted > 0:
                    n_undeleted -= 1
                else:
                    res_lis.append(ch)
        
        res = ''.join(res_lis) + '*' * n_undeleted
        return res[::-1]
        
"""
https://leetcode.cn/problems/removing-stars-from-a-string/submissions/564536744/?envType=daily-question&envId=2024-09-14

通过
零知识证明
零知识证明
提交于 2024.09.14 00:51

执行用时分布
149
ms
击败
40.23%

消耗内存分布
17.45
MB
击败
80.81%
"""
