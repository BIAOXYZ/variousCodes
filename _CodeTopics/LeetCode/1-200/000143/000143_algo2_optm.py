# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # 上一个原地的算法竟然超时了。。。所以其实就是得搞有额外空间但是快的呗。。。来了~
        # 先用最基本的list（就不信还会超时），然后再写个deque的。

        nodeArr, curr = deque([]), head
        while curr:
            nodeArr.append(curr)
            curr = curr.next

        if len(nodeArr) <= 2:
            return head
        
        while nodeArr:
            currHead = nodeArr.popleft()
            if nodeArr:
                currTail = nodeArr.pop()
            else:
                # 断开最后的单个节点的链接，否则会成环。
                currHead.next = None
                break
            currHead.next = currTail
            currTail.next = nodeArr[0] if nodeArr else None
        return head
        
"""
https://leetcode-cn.com/submissions/detail/117167996/

13 / 13 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 32.8 MB

执行用时：76 ms, 在所有 Python 提交中击败了96.92%的用户
内存消耗：32.8 MB, 在所有 Python 提交中击败了5.63%的用户
"""
"""
前一个提交和这个基本一模一样，就是list换deque，然后里面一处pop(0)换成popleft()。结果时间从超越7.00%变成96.92%。。。deque牛啤！
"""
