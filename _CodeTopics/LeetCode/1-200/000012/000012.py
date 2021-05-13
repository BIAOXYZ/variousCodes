class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        res = ""
        nums = [1000, 500, 100, 50, 10, 5, 1]
        letters = ["M", "D", "C", "L", "X", "V", "I"]

        i = 0
        flag = 0
        while num > 0:
            if num >= nums[i]:
                res += letters[i]
                num -= nums[i]
                flag += 1
                if flag == 4:
                    res = res[:-4] + letters[i] + letters[i-1]
                    if len(res) > 2 and res[-3] == res[-1]:
                        res = res[:-3] + letters[i] + letters[i-2]
            else:
                i += 1
                flag = 0
        return res
        
"""
https://leetcode-cn.com/submissions/detail/177308458/

3999 / 3999 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 13.1 MB

执行用时：56 ms, 在所有 Python 提交中击败了70.77%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了19.03%的用户
"""
