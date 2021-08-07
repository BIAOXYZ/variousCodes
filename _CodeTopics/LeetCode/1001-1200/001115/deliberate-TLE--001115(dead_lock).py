import threading
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.fooDone = threading.Lock()
        self.fooDone.acquire()
        self.barDone = threading.Lock()
        # 下面这句如果不注释掉，就死锁了。故意提交一把，加深下理解和记忆。
        self.barDone.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.barDone.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.fooDone.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.fooDone.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.barDone.release()
    
"""
https://leetcode-cn.com/submissions/detail/204445938/

0 / 144 个通过测试用例
状态：超出时间限制

最后执行的输入：
1
"""
