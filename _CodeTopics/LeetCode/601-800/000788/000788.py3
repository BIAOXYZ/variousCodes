class Solution:
    def rotatedDigits(self, n: int) -> int:

        res = 0
        unRotatable = ['3', '4', '7']
        dic = {
            '0':'0', '1':'1', '8':'8',
            '2':'5', '5':'2', '6':'9', '9':'6'
        }
        for num in range(2, n+1):
            s = list(str(num))
            if any([ch in unRotatable for ch in s]):
                continue
            rotatedS = ''.join(map(lambda x : dic[x], s))
            if int(rotatedS) != num:
                res += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/366978114/

执行用时：
144 ms
, 在所有 Python3 提交中击败了
7.26%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
83.87%
的用户
通过测试用例：
50 / 50
"""
