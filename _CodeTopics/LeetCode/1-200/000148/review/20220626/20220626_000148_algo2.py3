# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2):
            dummyHead = ListNode()
            cur = dummyHead
            while node1 and node2:
                if node1.val > node2.val:
                    cur.next = node2
                    node2 = node2.next
                else:
                    cur.next = node1
                    node1 = node1.next
                cur = cur.next
            if node1:
                cur.next = node1
            if node2:
                cur.next = node2
            return dummyHead.next
        def find_middle(node):
            # 对于 slow 和 fast 都从 dummyHead 出发的写法，
            # 如果是偶数个节点的话，最终 slow 停留在中间靠左的节点。
            # （但如果都从 head 出发，节点总数是偶数，最终 slow 停留在中间靠右的节点）
            dummyHead = ListNode()
            dummyHead.next = node
            slow = fast = dummyHead
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        if not head or not head.next:
            return head
        mid = find_middle(head)
        midNodeOrMidRightNode = mid.next
        # `000148_algo2.py` 把这个从中间断开的操作放到寻找链表中点的函数里面了，明显不太好。
        mid.next = None
        return merge(self.sortList(head), self.sortList(midNodeOrMidRightNode))
        
"""
https://leetcode.cn/submissions/detail/329320764/

执行用时：
636 ms
, 在所有 Python3 提交中击败了
18.02%
的用户
内存消耗：
35.1 MB
, 在所有 Python3 提交中击败了
30.05%
的用户
通过测试用例：
30 / 30
"""
