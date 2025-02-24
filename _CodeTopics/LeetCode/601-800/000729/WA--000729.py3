class MyCalendar:

    def __init__(self):
        self.cld = set()

    def book(self, startTime: int, endTime: int) -> bool:
        for schedule in self.cld:
            st, et = schedule
            if startTime >= et or endTime < st:
                continue
            else:
                return False
        self.cld.add((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

"""
https://leetcode.cn/problems/my-calendar-i/submissions/602613393

解答错误
79 / 107 个通过的测试用例

输入
["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
输出
[null,true,true,false,false,true,false,false,true,true,false]
预期结果
[null,true,true,false,false,true,false,true,true,true,false]
"""
