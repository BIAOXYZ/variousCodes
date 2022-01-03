class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        # "1971.1.1" 是周五
        # 这题算简单有点过了吧？。。。

        dic = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        totalDays = 0

        totalDays += 365 * (year - 1971)
        nextLeapYear = 1972
        # 这里改用大于号，而不是大于等于，是为了表示“只有超出整年的，才在年的部分里计算”。
        # 这样如果目标年份恰好是闰年，会放到月份里去计算。这个更合乎逻辑。
        while year > nextLeapYear:
            totalDays += 1
            nextLeapYear += 4
            if nextLeapYear % 100 == 0 and nextLeapYear % 400 != 0:
                nextLeapYear += 4
        
        # 如果是1月，月的部分只加上0天，剩下的放到日的部分里去算。
        monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        totalDays += sum(monthDays[:month])  
        # if year == nextLeapYear and (month > 2 or (month == 2 and day == 29)):
        # 这里原来写的是上面那句，结果会导致闰年的二月29会出错，比如 1972.2.29。原因是如果恰好处于 2.29 当天，
        # 那么这一天还没过完，所以不能加上。。。
        if year == nextLeapYear and month > 2:
            totalDays += 1
        
        totalDays += day - 1

        return dic[(5 + totalDays) % 7]
        
"""
https://leetcode-cn.com/submissions/detail/254487981/

执行用时：40 ms, 在所有 Python3 提交中击败了13.50%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.22%的用户
通过测试用例：
43 / 43
"""
