class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        for elem in arr:
            flag = False
            for lis in pieces:
                if lis and elem == lis[0]:
                    flag = True
                    lis.pop(0)
            if not flag:
                return False
        return True
        
"""
https://leetcode.cn/submissions/detail/365785960/

81 / 84 个通过测试用例
状态：解答错误

输入：
[1,2,3]
[[2],[1,3]]
输出：
true
预期结果：
false
"""
