# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        def get_node_by_index(head, ind=-1):
            cur = head
            pre = None
            num = 0
            while cur:
                if num == ind:
                    return cur
                pre = cur
                cur = cur.next
                num += 1
            return pre if ind == -1 else None
        
        preA = get_node_by_index(list1, a-1)
        nextB = get_node_by_index(list1, b+1)
        list2Tail = get_node_by_index(list2, -1)
        preA.next = list2
        list2Tail.next = nextB
        return list1
        
"""
https://leetcode.cn/submissions/detail/397955876/

执行用时：
392 ms
, 在所有 Python3 提交中击败了
31.95%
的用户
内存消耗：
21.4 MB
, 在所有 Python3 提交中击败了
93.49%
的用户
通过测试用例：
61 / 61
"""
