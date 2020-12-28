class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        
        self.ptr = 1
        self.arr = [0] * (n+1)

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        
        self.arr[id] = value
        if self.arr[self.ptr] == 0:
            return []
        start = self.ptr
        while self.ptr <= len(self.arr)-1 and self.arr[self.ptr] != 0:
            self.ptr += 1
        return self.arr[start:self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)

"""
https://leetcode-cn.com/submissions/detail/123516424/

101 / 101 个通过测试用例
状态：通过
执行用时: 616 ms
内存消耗: 13.3 MB
"""
