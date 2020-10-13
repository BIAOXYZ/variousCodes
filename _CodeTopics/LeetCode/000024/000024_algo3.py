# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if not head or not head.next:
        #     return head
        
        dummyHead, dummyHead.next = ListNode(0), head
        curr = dummyHead

        while curr.next and curr.next.next:
            node1, node2 = curr.next, curr.next.next
            # 以当前要交换的两个节点的前一个节点为中心的“视角”来处理。
            node1.next = node2.next
            node2.next = node1
            curr.next = node2
            # 为下一轮交换赋值，官方答案这种引入dummyHead的话更简单些，只需要把curr更新就行。
            # 因为进到下一轮while循环，如果curr的后两个节点都非空才继续更新node1和node2。
            curr = node1
        return dummyHead.next
        
"""
https://leetcode-cn.com/submissions/detail/115582480/

55 / 55 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了69.71%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了5.00%的用户
"""
