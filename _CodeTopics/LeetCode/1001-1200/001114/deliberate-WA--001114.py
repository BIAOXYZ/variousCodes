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
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        # 这里，以及下面还得有一个拿锁的过程，所以故意提交错一次。
        self.secondJobDone.release()

            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
"""
https://leetcode-cn.com/submissions/detail/204269612/

4 / 36 个通过测试用例
状态：解答错误

最后执行的输入：
[1,3,2]
输出：
"thirdsecondfirst"
预期结果：
"firstsecondthird"
"""
