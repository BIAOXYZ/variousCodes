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

        if not head or not head.next:
            return head
        
        res = head.next
        preNode, currNode, nextNode = None, head, head.next

        while True:
            if currNode:
                if nextNode:
                    # 交换两节点指向
                    nextnext = nextNode.next
                    nextNode.next = currNode
                    currNode.next = nextnext
                    # 加上这句就可以省掉第一次对head和head.next进行处理时的重复代码了。（详情参见 000024.py）
                    # 这个if只有第一次进while循环时不执行，后面都要执行。其实也就对应了现实的情况：
                    # 只有head和head.next的交换不需要处理preNode，后面的交换需要处理preNode。
                    if preNode:
                        preNode.next = nextNode
                    # 为下一轮交换赋值
                    preNode, currNode = currNode, nextnext
                    if currNode:
                        nextNode = currNode.next
                else:
                    break
            else:
                break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/115391385/

55 / 55 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.4 MB

执行用时：24 ms, 在所有 Python 提交中击败了43.33%的用户
内存消耗：12.4 MB, 在所有 Python 提交中击败了89.79%的用户
"""
