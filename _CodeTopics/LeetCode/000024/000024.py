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
        currNode, nextNode = head, head.next

        # 交换两节点指向
        nextnext = nextNode.next
        nextNode.next = currNode
        currNode.next = nextnext
        # 为下一轮交换赋值
        preNode, currNode = currNode, nextnext
        if currNode:
            nextNode = currNode.next

        while True:
            if currNode:
                if nextNode:
                    # 交换两节点指向
                    nextnext = nextNode.next
                    nextNode.next = currNode
                    currNode.next = nextnext
                    """
                    # 这里就是最容易出错的地方！！！第一对节点的交换不用考虑和之前节点preNode的连接问题，
                    # 但是后面每一对节点的交换必须考虑！
                    # 大概举例如下：假定输入是：1->2->3->4，第一次交换完成后变成 2->1->3->4 没问题。
                    # 紧接着currNode变为节点3，nextNode变为节点4，nextnext等于nextNode.next为None。
                    # nextNode.next = currNode 这句一执行完，以res为头节点的链表变为：2->1->3->4->3
                    # currNode.next = nextnext 这句再一执行完，以res为头节点的链表变为：2->1->3->None，
                      但是请注意，此时节点4仍旧指向节点3！
                    # 如果这时候不把节点4和前面的节点1连上就返回，当然意味着丢掉了节点4，也就是结果为[2,1,3]。
                    # 所以这里需要一个变量记录下前一个preNode，然后执行下面这句，从而使节点1指向节点4。
                    # PS：如果较长时间后忘了，就单步调试吧，准备把可调试的代码复制到该题的README里。
                    """
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
https://leetcode-cn.com/submissions/detail/115317462/

55 / 55 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.4 MB

执行用时：16 ms, 在所有 Python 提交中击败了89.04%的用户
内存消耗：12.4 MB, 在所有 Python 提交中击败了84.11%的用户
"""
