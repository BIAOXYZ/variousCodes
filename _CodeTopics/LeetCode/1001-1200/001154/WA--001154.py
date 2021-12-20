class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """

        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
        leapYearFlag = 1 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 0
        dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        res = 0
        for i in range(1, month):
            res += dic[i]
        res += day
        return res if not leapYearFlag else res + 1
        
"""
https://leetcode-cn.com/submissions/detail/250456216/

10537 / 10957 个通过测试用例
状态：解答错误

输入：
"2012-01-02"
输出：
3
预期结果：
2
"""
