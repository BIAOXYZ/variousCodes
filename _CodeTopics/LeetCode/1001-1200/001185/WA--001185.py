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
        
        monthDays = [-31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        totalDays += sum(monthDays[:month+1])
        
        totalDays += day - 1

        return dic[(5 + totalDays) % 7]
        
"""
https://leetcode-cn.com/submissions/detail/254392722/

29 / 43 个通过测试用例
状态：解答错误

输入：
29
2
2016
输出：
"Saturday"
预期结果：
"Monday"
"""
