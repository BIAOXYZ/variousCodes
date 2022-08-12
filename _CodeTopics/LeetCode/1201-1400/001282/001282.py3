class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        dic = {}
        res = []
        for i, num in enumerate(groupSizes):
            if num == 1:
                res.append([i])
            else:
                if num in dic:
                    dic[num].append(i)
                    if len(dic[num]) == num:
                        res.append(dic[num])
                        del dic[num]
                else:
                    dic[num] = [i]
        return res
        
"""
https://leetcode.cn/submissions/detail/349408517/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
77.48%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
87.84%
的用户
通过测试用例：
103 / 103
"""
