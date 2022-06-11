# 假定当前是 [1,2,3,4]，接着使用了一次 3，此时变成 [3,1,2,4]。
# 如果不使用链表类的结构，涉及数组移动的，也就是更新最近使用时间这个操作
# （get和put都会涉及这个操作的）是不可能为 O(1) 的。也就是必须得用类似链表的结构。

# 相对于第一次（`000146_ugly.py3`）的优化点：
# 1.不再使用两个字典，仅保留 key:node 这个字典，val 从 node 的 val 来获得。
# 2.对接口进行更进一步封装。
# 3.上一次有个失误就是经常不小心把 node.nxt 写出 node.next。如果在 C++ 里很容易通过
#   通过报错发现；但在 Python 里相当于给对象又添加了一个成员，是合法的操作，于是就不容易找出来。
#   于是后面可以有个教训：凡是成员都用四个字母的（next，prev），凡是变量都用三个字母的（nxt，pre，cur），
#   curr 以后就尽量别用了。。。
class Node:
    def __init__(self, key, val, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = pre
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            val = node.val
            self._remove_node(node)
            self._insert_node(node)
        else:
            val = -1
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self._remove_node(node)
        else:
            node = Node(key, value)
        self._insert_node(node)

    # 前面的代码部分保证了 insert_node 前这个 node 肯定已经不在链表里了。
    # 同样的，也保证了 remove_node 时这个 node 肯定在链表里。
    def _insert_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            oldHead = self.head
            node.next = oldHead
            oldHead.prev = node
            self.head = node
        self.dic[node.key] = node
        self.size += 1
        if self.size > self.cap:
            self._remove_node(self.tail)

    # 使用 dummyHead 和 dummyTail 的好处：很多地方可以省略掉那些判断节点是否为空的操作了。
    # 纯用 head 和 tail，感觉真是不好写，一堆 if 判断。
    def _remove_node(self, node):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.size > 1:
            if node == self.tail:
                nodePre = node.prev
                nodePre.next = None
                self.tail = nodePre
            elif node == self.head:
                nodeNxt = node.next
                nodeNxt.prev = None
                self.head = nodeNxt
            # 因为既不等于 head 也不等于 tail，此时隐含了至少有 3 个节点。
            else:
                nodePre, nodeNxt = node.prev, node.next
                nodePre.nxt = nodeNxt
                nodeNxt.pre = nodePre
        # node.prev = None
        # node.next = None
        self.dic.pop(node.key)
        self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
https://leetcode.cn/submissions/detail/324178178/

14 / 21 个通过测试用例
状态：解答错误

输入：
["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
[[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
输出：
[null,null,null,null,null,4,3,2,-1,null,-1,2,-1,4,5]
预期结果：
[null,null,null,null,null,4,3,2,-1,null,-1,2,3,-1,5]
"""
"""
就是想改一下 `000146_ugly.py3`，封装一下接口，写更好（记）点，结果还错了。。。服了。
"""
