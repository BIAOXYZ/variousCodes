# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self._next = iterator.next()
        self._hasNext = iterator.hasNext()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next


    def next(self):
        """
        :rtype: int
        """
        res = self._next
        self._hasNext = self.it.hasNext()
        self._next = self.it.next() if self._hasNext else -1
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._hasNext
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

"""
https://leetcode-cn.com/submissions/detail/225803948/

14 / 14 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了55.56%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了85.19%的用户
"""
