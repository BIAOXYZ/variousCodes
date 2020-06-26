class Solution:
    def translateNum(self, num: int) -> int:
        numstr = str(num)
        length = len(numstr)

        if length == 1:
            return 1
        elif length == 2:
            if num > 25:
                return 1
            else:
                return 2
        else:
            if int(numstr[0:2]) > 25:
                return self.translateNum(int(numstr[1:]))
            else:
                return self.translateNum(int(numstr[1:])) + self.translateNum(int(numstr[2:]))
                
"""
# https://leetcode-cn.com/submissions/detail/77485941/

49 / 49 个通过测试用例
	状态：通过
执行用时：44 ms
内存消耗：13.7 MB
"""
"""
# 完全一模一样的代码，发现python3还没python2快？当然也可能是偶尔一次执行的偏差，但是懒得去多次试了。

执行结果：通过
显示详情
执行用时 :44 ms, 在所有 Python3 提交中击败了40.55% 的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
"""
"""
# 这是上一个python2的：

执行结果：通过
显示详情
执行用时 :16 ms, 在所有 Python 提交中击败了86.61% 的用户
内存消耗 :12.6 MB, 在所有 Python 提交中击败了100.00%的用户
"""
