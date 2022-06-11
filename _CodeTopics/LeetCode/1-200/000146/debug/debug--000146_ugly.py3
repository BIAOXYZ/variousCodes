
import sys
from functools import reduce
import bisect
from collections import defaultdict, Counter



# 假定当前是 [1,2,3,4]，接着使用了一次 3，此时变成 [3,1,2,4]。
# 如果不使用链表类的结构，涉及数组移动的，也就是更新最近使用时间这个操作
# （get和put都会涉及这个操作的）是不可能为 O(1) 的。也就是必须得用类似链表的结构。
class Node:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.dic = {}
        self.keyNodeDic = {}
        self.dummyHead = Node(-1)
        self.tail = None

    def get(self, key: int) -> int:
        ## print("call get")
        if key in self.dic:
            val = self.dic[key]
            self.move_to_first(key)
        else:
            val = -1
        return val

    def put(self, key: int, value: int) -> None:
        ## print("call put")
        self.dic[key] = value
        self.move_to_first(key)

    def move_to_first(self, key) -> None:
        ## print("call move_to_first")
        head = self.dummyHead.nxt
        if key in self.keyNodeDic:
            node = self.keyNodeDic[key]
            # 如果 node 等于 dummyHead 的 next，那就没必要做任何动作了。
            if node != head:
                # 如果当前 node 是一个中间节点
                if node != self.tail:
                    # 提取出要用到的其他节点
                    nodePre, nodeNxt = node.pre, node.nxt
                    # node 移到第一个位置（最活跃位置）
                    self.dummyHead.nxt = node
                    node.nxt = head
                    head.pre = node
                    # 处理node前后的节点
                    nodePre.nxt = nodeNxt
                    nodeNxt.pre = nodePre
                # 如果当前 node 恰好是最后一个节点
                elif node == self.tail:
                    # 提取出要用到的其他节点
                    nodePre = node.pre
                    # node 移到第一个位置（最活跃位置）
                    self.dummyHead.nxt = node
                    node.nxt = head
                    head.pre = node
                    # 处理尾节点
                    nodePre.nxt = None
                    self.tail = nodePre
        else:
            node = Node(key)
            self.keyNodeDic[key] = node
            if self.size < self.cap:
                if not head:
                    self.dummyHead.nxt = node
                    self.tail = node
                else:
                    self.dummyHead.nxt = node
                    node.nxt = head
                    head.pre = node
                self.size += 1
            elif self.size == self.cap:
                self.dummyHead.nxt = node
                node.nxt = head
                head.pre = node
                # 删除最后一个节点，更新尾节点
                tailKey = self.tail.val
                self.tail = self.tail.pre
                self.tail.nxt = None
                del self.dic[tailKey]
                del self.keyNodeDic[tailKey]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Test():
    def run(self, rotatedArr, num):
        sol = Solution()
        res = sol.binarySearch(rotatedArr, num)
        #print ("The indices for the list %s to obtain %s is %s" % (listofnums, targetvalue, res))

if  __name__ == '__main__':
    print("------------------------------\nThe main program will start!\n------------------------------\n")
    print("The default coding is:", sys.getdefaultencoding())
    print("\n")


    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
    lru.get(2)
    lru.put(4, 4)
    lru.get(1)
    lru.get(3)
    lru.get(4)


    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")

