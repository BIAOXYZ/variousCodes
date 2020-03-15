class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxlen = maxSize
        self.currlen = 0
        self.val = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.currlen < self.maxlen:
            # self.val[self.currlen] = x 
            ## IndexError: list assignment index out of range, 原因是下一个值本来就没有，所以应该用append方法。
            self.val.append(x)
            self.currlen += 1
        else:
            pass
        

    def pop(self):
        """
        :rtype: int
        """
        if self.currlen > 0:
            number = self.val[self.currlen-1]
            self.val.pop()
            self.currlen -= 1
            return number
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if k < self.currlen:
            for i in range(k):
                self.val[i] = self.val[i] + val
        else:
            for i in range(self.currlen):
                self.val[i] = self.val[i] + val

                
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
