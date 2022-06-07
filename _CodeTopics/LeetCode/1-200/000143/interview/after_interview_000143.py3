# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        n = len(nodes)
        left, right = 0, n-1
        dummyPrev = ListNode(-1)
        while left < right:
            dummyPrev.next = nodes[left]
            nodes[left].next = nodes[right]
            dummyPrev = nodes[right]
            left += 1
            right -= 1
        # 奇数个节点的情况
        if left == right:
            dummyPrev.next = nodes[left]
            nodes[left].next = None
        # 偶数个节点的情况
        elif left > right:
            nodes[left].next = None
        return head
        
"""
https://leetcode.cn/submissions/detail/322801086/

执行用时：
80 ms
, 在所有 Python3 提交中击败了
50.03%
的用户
内存消耗：
23.1 MB
, 在所有 Python3 提交中击败了
83.88%
的用户
通过测试用例：
12 / 12
"""
