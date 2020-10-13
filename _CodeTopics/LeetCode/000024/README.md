
`24. 两两交换链表中的节点` https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/
- [x] 方法一：递归
- [x] 方法二：迭代

# 测试用例

```console
[]
[1]
[1,2]
[1,2,3]
[1,2,3,4]
[1,2,3,4,5]
[1,2,3,4,5,6]
```

# `deliberate-WA--000024.py`

本地用于调试的版本，借用了这道题的playground里的辅助函数`stringToListNode()`：
```py
# -*- coding: utf-8 -*-
import sys


import json
def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
        
        while True:
            if currNode:
                if nextNode:
                    # 交换两节点指向
                    nextnext = nextNode.next
                    nextNode.next = currNode
                    currNode.next = nextnext
                    # 为下一轮交换赋值
                    currNode = nextnext
                    if currNode:
                        nextNode = currNode.next
                else:
                    break
            else:
                break
        return res

class Test():
    def run(self, head):
        sol = Solution()
        res = sol.swapPairs(head)
        #print ("The indices for the list %s to obtain %s is %s" % (listofnums, targetvalue, res))

if  __name__ == '__main__':
    print("------------------------------\nThe main program will start!\n------------------------------\n")
    print("The default coding is:", sys.getdefaultencoding())
    print("\n")

    # node2 = ListNode(2)
    # node1 = ListNode(1)
    # node1.next = node2

    line = "[1,2,3,4]"
    head = stringToListNode(line)

    test = Test()
    test.run(head)

    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")
    
```

# `000024.py` --> `000024_impl.py` --> `000024_impl2.py` --> `000024_impl3.py`

`000024.py` --> `000024_impl.py` --> `000024_impl2.py` --> `000024_impl3.py` 是一个不断优化的过程：
- `000024.py`：需要额外的逻辑处理`head`和`head.next`，但是这部分和general的交换两节点其实只有一点不同。
- `000024_impl.py`：可以不用额外的逻辑处理`head`和`head.next`了。
- `000024_impl2.py`：不使用while True了，但是里面还得自己break一层。
- `000024_impl3.py`：无需自己手动break出while循环的逻辑了。
