class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        # "1971.1.1" 是周五
        # 这题算简单有点过了吧？。。。

        dic = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        totalDays = 0

        totalDays += 365 * (year - 1971)
        nextLeapYear = 1972
        while year >= nextLeapYear:
            if year > nextLeapYear or (year == nextLeapYear and (month > 2 or (month == 2 and day == 29))):
                totalDays += 1
            nextLeapYear += 4
            if nextLeapYear % 100 == 0 and nextLeapYear % 400 != 0:
                nextLeapYear += 4
        
        monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        totalDays += sum(monthDays[:month])
        
        if month == 2 and day == 29:
            totalDays += day - 2
        else:
            totalDays += day - 1

        return dic[(5 + totalDays) % 7]
        
"""
https://leetcode-cn.com/submissions/detail/254394924/

执行用时：28 ms, 在所有 Python3 提交中击败了89.88%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了18.10%的用户
通过测试用例：
43 / 43
"""
