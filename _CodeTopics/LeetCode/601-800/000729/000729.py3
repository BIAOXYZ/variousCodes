class MyCalendar:

    def __init__(self):
        self.cld = set()

    def book(self, startTime: int, endTime: int) -> bool:
        for schedule in self.cld:
            st, et = schedule
            if startTime >= et or endTime <= st:
                continue
            else:
                return False
        self.cld.add((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

"""
https://leetcode.cn/problems/my-calendar-i/submissions/613319794/

通过
107 / 107 个通过的测试用例

执行用时分布
294
ms
击败
43.06%
复杂度分析
消耗内存分布
18.34
MB
击败
76.72%
"""
