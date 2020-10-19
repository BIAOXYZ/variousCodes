# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        """
        思想：基本想法就是二分查找到中间值作为（子树）根节点，然后递归下去。前一半
              是左子树，后一半是右子树。且因为是有序的，直接取中间就行，二分都省了。
        """

        root = TreeNode()
        left, right = 0, len(nums)-1
        if nums:
            mid = left + (right - left) >> 1
            root.val = nums[mid]
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
        return None
        
"""
https://leetcode-cn.com/submissions/detail/84163985/

32 / 32 个通过测试用例
状态：通过
执行用时：36 ms
内存消耗：17.3 MB
"""
"""
# 从几组输出看，我的实现似乎对一些null优化得不够。比如假定输入为 [1,2,3,4,5,6]，我的结果null就比官方答案多。
# 其他的输入也是类似的情况，所以可以再看看怎么优化。
``
             3
       1          5
 null     2    4     6
``
``
             4
       2          6
   1       3   5
``

输入
[-10,-3,0,5,9]
[1,2,3,4,5,6]
[1,2,3,4,5]

输出
[0,-10,5,null,-3,null,9]
[3,1,5,null,2,4,6]
[3,1,4,null,2,null,5]

预期结果
[0,-3,9,-10,null,5]
[4,2,6,1,3,5]
[3,2,5,1,null,4]
"""
