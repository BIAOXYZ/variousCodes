class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        res = []
        for num in range(left, right+1):
            lst = list(str(num))
            if '0' in lst:
                continue
            if all(num % int(digit) == 0 for digit in lst):
                res.append(num)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/292350739/

执行用时：
64 ms
, 在所有 Python3 提交中击败了
17.36%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
38.84%
的用户
通过测试用例：
31 / 31
"""
