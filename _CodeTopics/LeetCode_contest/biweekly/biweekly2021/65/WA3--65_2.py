class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.w = width - 1
        self.h = height - 1
        if width > 2 and height > 2:
            self.loop = 2 * width + 2 * height - 4
        else:
            self.loop = width * height
        self.x = 0
        self.y = 0

    def move(self, num):
        """
        :type num: int
        :rtype: None
        """
        num = num % self.loop
        while num > 0:
            if self.x < self.w and self.y == 0:
                self.x += 1
            elif self.x == self.w and self.y < self.h:
                self.y += 1
            elif self.x > 0 and self.y == self.h:
                self.x -= 1
            elif self.x == 0 and self.y > 0:
                self.y -= 1
            num -= 1

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.x, self.y]

    def getDir(self):
        """
        :rtype: str
        """
        if 0 < self.x <= self.w and self.y == 0:
            return "East"
        elif self.x == self.w and 0 < self.y <= self.h:
            return "North"
        elif 0 <= self.x < self.w and self.y == self.h:
            return "West"
        elif self.x == 0 and 0 <= self.y < self.h:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

"""
https://leetcode-cn.com/submissions/detail/238364626/

139 / 142 个通过测试用例
状态：解答错误

输入：
Hidden for this testcase during contest.
输出：
Hidden for this testcase during contest.
预期：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.
"""
