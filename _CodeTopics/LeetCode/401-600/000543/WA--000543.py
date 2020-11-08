# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_node_num_in_path(node):
            if not node:
                return 0
            return 1 + max(max_node_num_in_path(node.left), max_node_num_in_path(node.right))
        
        if not root:
            return 0
        """
        leftSubtreeLen = 0 if not root.left else max_node_num_in_path(root.left) - 1
        rightSubtreeLen = 0 if not root.right else max_node_num_in_path(root.right) - 1
        return leftSubtreeLen + rightSubtreeLen + 2

        最开始写成上面的形式，但是有些问题。如果某个孩子为空，其实那个1就不该算上了，所以后面加2会多加。
        比如这个输入：[1,2,null,4,5]
        """
        # 直接用下面这句就可以，是因为：如果某个孩子本来就是空，那么相当于加了0；如果不是空，比如有两个点，
        # 按理说子树路径是2-1，但是连着root节点的还应该再加上1，所以下面这个是对的。
        return max_node_num_in_path(root.left) + max_node_num_in_path(root.right)
        
"""
https://leetcode-cn.com/submissions/detail/121894871/

102 / 106 个通过测试用例
状态：解答错误

输入：
[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
输出：
7
预期：
8
"""
