class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # 先把几个特殊情况直接不处理了。。。
        dic = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        if num in dic:
            return dic[num]

        res = ""
        nums = [1000, 500, 100, 50, 10, 5, 1]
        letters = ["M", "D", "C", "L", "X", "V", "I"]

        i = 0
        while num > 0:
            if num >= nums[i]:
                res += letters[i]
                num -= nums[i]
            else:
                i += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/177307955/

2053 / 3999 个通过测试用例
状态：解答错误

最后执行的输入：
1994
"""
