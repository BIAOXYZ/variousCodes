# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        # 这个基本就是官方答案的写法，主要是为了记录下 random 包里的这个函数。
        return random.choice(self.arr)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
https://leetcode-cn.com/submissions/detail/258871353/

执行用时：52 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了8.85%的用户
通过测试用例：
8 / 8
"""
