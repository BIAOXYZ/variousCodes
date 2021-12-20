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
        return res + 1 if leapYearFlag and month > 2 else res
        
"""
https://leetcode-cn.com/submissions/detail/250456497/

执行用时：116 ms, 在所有 Python 提交中击败了76.27%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了94.92%的用户
通过测试用例：
10957 / 10957
"""
