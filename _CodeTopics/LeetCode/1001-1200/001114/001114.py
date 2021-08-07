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
        
        self.firstJobDone.acquire()
        try:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.secondJobDone.release()
        finally:
            self.firstJobDone.release()
        
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        self.secondJobDone.acquire()
        try:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
        finally:
            self.secondJobDone.release()
        
"""
https://leetcode-cn.com/submissions/detail/204277628/

36 / 36 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.2 MB

执行用时：36 ms, 在所有 Python 提交中击败了45.11%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了51.13%的用户
"""
"""
- 参考了官方文档：用with的锁的写法就是后面帮你自动release掉，跟用with开文件是一样的，最后会自动帮你close掉文件。
  https://docs.python.org/3/library/threading.html#with-locks
- TODO：看起来执行用时比用with的方式慢了很多，不知道是偶然现象还是with的写法效率就是高。。。
  也可能是 try...finally... 引起的低效率？
"""
