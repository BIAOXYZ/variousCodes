import threading
class Foo(object):
    def __init__(self):
        self.firstJobDone = threading.Lock()
        self.secondJobDone = threading.Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.firstJobDone.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        with self.firstJobDone:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.secondJobDone.release()
        
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        with self.secondJobDone:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
        
"""
https://leetcode-cn.com/submissions/detail/204274627/

36 / 36 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了90.23%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了88.72%的用户
"""
