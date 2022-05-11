# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        # 少了下面这行就要在 121212 之间死循环了。
        # pre.next = None
        
        while cur:
            nxt = cur.next
            cur.next = pre
            # 如果不在上面处理一次 head 的 next，那么就要在这里用个 if 分支来处理。这种特殊处理无法避免，原因如下：
            # 因为，可以这样想，以输入 [1,2,3,4,5] 为例：
            ## 第一次 while 循环时，pre 和 cur 是 1 和 2，且在本次循环体里，（需要）同时处理 1 和 2 的 next；
            ## 但是下次 2 和 3 分别是 pre 和 cur 的时候，2 的 next 之前已经处理过了，这里只需要处理 3 的 next；
            ## 后面到 3 和 4 的时候，3 的 next 肯定也处理过了，只需要处理 4 的 next，依次类推。
            # 所以，一个 while 循环最好只处理一次，也就是 cur 的 next！！！
            ## 也就是说，head 的 next 比较特殊，最好的方式就是在开头就处理下。
            if pre is head:
                pre.next = None
            pre = cur
            cur = nxt
        return pre
        
"""
https://leetcode.cn/submissions/detail/312336629/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
87.80%
的用户
内存消耗：
16.1 MB
, 在所有 Python3 提交中击败了
46.59%
的用户
通过测试用例：
28 / 28
"""
"""
2022.05.12 （要面Azure之前——虽然主要只是想练手了）再次总结。
"""
