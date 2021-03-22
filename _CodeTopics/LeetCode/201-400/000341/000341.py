# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
# 补充下，如果nestedList只是个标准的List，下面的代码就可以了。最开始就是当成普通List写的函数。
# ——> 偏偏它是个自定义的类。。。无趣。。。

def get_list_element(lis):
    res = []
    for elem in lis:
        if type(elem) != type(list()):
            res.append(elem)
        else:
            for elem2 in get_list_element(elem):
                res.append(elem2)
    return res

l = [[1,1],2,[1,1,[4,5]]]
res = get_list_element(l)
print (res)
--------------------------------------------------
[1, 1, 2, 1, 1, 4, 5]
"""

class NestedIterator(object):
    currOffset = 0
    iterator = []

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def get_list_element(nlis):
            res = []
            for elem in nlis:
                if elem.isInteger():
                    res.append(elem.getInteger())
                else:
                    res.extend(get_list_element(elem.getList()))
            return res
        self.iterator = get_list_element(nestedList)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:
            res = self.iterator[self.currOffset]
            self.currOffset += 1
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.currOffset < len(self.iterator):
            return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

"""
https://leetcode-cn.com/submissions/detail/158557892/

44 / 44 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 18.9 MB

执行用时：56 ms, 在所有 Python 提交中击败了83.33%的用户
内存消耗：18.9 MB, 在所有 Python 提交中击败了11.46%的用户
"""
