# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = {}
        ind = 0
        while head:
            self.nodes[ind] = head.val
            head = head.next
            ind += 1
        self.length = ind

    def getRandom(self) -> int:
        randomIndex = random.randint(0, self.length-1)
        return self.nodes[randomIndex]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
https://leetcode-cn.com/submissions/detail/258870156/

执行用时：76 ms, 在所有 Python3 提交中击败了83.78%的用户
内存消耗：18.1 MB, 在所有 Python3 提交中击败了5.01%的用户
通过测试用例：
8 / 8
"""
