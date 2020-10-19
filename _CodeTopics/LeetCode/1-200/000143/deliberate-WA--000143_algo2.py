# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # 上一个原地的算法竟然超时了。。。所以其实就是得搞有额外空间但是快的呗。。。来了~
        # 先用最基本的list（就不信还会超时），然后再写个deque的。

        """
        []
        [1]
        [1,2]
        [1,2,3]
        [1,2,3,4]
        [1,2,3,4,5]
        [1,2,3,4,5,6]

        对于上面的测试用例，输出是：

        []
        [1]
        [1,2]
        Error - Found cycle in the ListNode
        [1,4,2,3]
        Error - Found cycle in the ListNode
        [1,6,2,5,3,4]

        应该是奇数长度的链表搞出来环了，一会修改代码就是了。
        这里故意提交一下主要就是因为这个Error还是第一次见到。
        """
        nodeArr, curr = [], head
        while curr:
            nodeArr.append(curr)
            curr = curr.next
        
        if len(nodeArr) <= 2:
            return head
        
        while nodeArr:
            currHead = nodeArr.pop(0)
            if nodeArr:
                currTail = nodeArr.pop()
            else:
                break
            currHead.next = currTail
            currTail.next = nodeArr[0] if nodeArr else None
        return head
        
"""
https://leetcode-cn.com/submissions/detail/117094702/

6 / 13 个通过测试用例
状态：解答错误

输入：
[1,2,3,4,5]
输出：
Error - Found cycle in the ListNode
预期：
[1,5,2,4,3]
"""
