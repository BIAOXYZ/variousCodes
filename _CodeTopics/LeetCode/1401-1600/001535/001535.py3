class LinkedListNode:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        n = len(arr)
        if n == 2 or k >= n - 1:
            return max(arr)

        def list_to_linkedlist(lis):
            dummyHead = LinkedListNode(-1)
            curr = dummyHead
            for elem in lis:
                node = LinkedListNode(val=elem, pre=curr)
                curr.nxt = node
                curr = node
            tail = curr
            head = dummyHead.nxt
            dummyHead.nxt = None
            head.pre = None
            return head, tail
        
        head, tail = list_to_linkedlist(arr)
        res, winningRounds = None, 0
        while winningRounds < k:
            # 由于数组长度为 2 的情况前面已经直接return了，所以这里 thirdNode 一定会存在的
            firstNode, secondNode, thirdNode = head, head.nxt, head.nxt.nxt
            firstNum, secondNum = head.val, head.nxt.val
            maxNum, minNum = max(firstNum, secondNum), min(firstNum, secondNum)
            
            # 核心思想就是：
            ## 1. 永远把第一个节点的值换一下，换成最大值就行；
            ## 2. 然后第二个节点永远删除掉；
            ## 3. 最后把两个值里的较小值形成新节点，放在链表尾部。

            firstNode.val = maxNum
            firstNode.nxt = thirdNode
            thirdNode.pre = firstNode
            secondNode.pre = secondNode.nxt = None
            
            newTail = LinkedListNode(minNum)
            tail.nxt = newTail
            newTail.pre = tail
            tail = newTail

            if res == maxNum:
                winningRounds += 1
            else:
                res = maxNum
                winningRounds = 1
        return res

"""
https://leetcode.cn/problems/find-the-winner-of-an-array-game/submissions/533070809?envType=daily-question&envId=2024-05-19

通过
提交于 2024.05.19 14:51

执行用时分布
266
ms
击败
10.29%
使用 Python3 的用户
消耗内存分布
38.52
MB
击败
5.88%
使用 Python3 的用户
"""
