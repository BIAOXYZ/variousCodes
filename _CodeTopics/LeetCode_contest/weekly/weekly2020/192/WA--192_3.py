class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.backstack = []
        self.forwardstack = []
        self.curr = homepage
        return None

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.backstack.append(self.curr)
        self.forwardstack = []
        self.curr = url
        return None

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        lenb = len(self.backstack)
        if lenb == 0:
            return self.curr
        
        self.forwardstack.append(self.curr)
        loopnum = min(lenb, steps - 1)
        for i in range(loopnum-1):
            self.forwardstack.append(self.backstack[-1])
            self.backstack.pop()
        self.curr = self.backstack[-1]
        self.forwardstack.append(self.backstack[-1])
        self.backstack.pop()
        return self.curr

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        lenf = len(self.forwardstack)
        if lenf == 0:
            return self.curr
        
        self.backstack.append(self.curr)
        loopnum = min(lenf, steps - 1)
        for i in range(loopnum-1):
            self.backstack.append(self.forwardstack[-1])
            self.forwardstack.pop()
        self.curr = self.forwardstack[-1]
        self.backstack.append(self.forwardstack[-1])
        self.forwardstack.pop()
        return self.curr

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

"""
# https://leetcode-cn.com/submissions/detail/76938451/

6 / 71 个通过测试用例
	状态：解答错误

输入：["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
      [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
输出：[null,null,null,null,"facebook.com","google.com","google.com",null,"linkedin.com","google.com","leetcode.com"]
预期：[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
"""
