# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def is_leaf(node):
            return True if not node.left and not node.right else False
        def calculate_min_camera_of_node(node):
            if not node:
                return 0, 0
            with_camera, without_camera = node.val / 10000, node.val % 10000
            return with_camera, without_camera
        
        def dfs_and_dp(node):
            if is_leaf(node):
                node.val = 10001
                return
            else:
                if node.left:
                    dfs_and_dp(node.left)
                left_with_camera, left_without_camera = calculate_min_camera_of_node(node.left)
                min_left = min(left_with_camera, left_without_camera)
                if node.right:
                    dfs_and_dp(node.right)
                right_with_camera, right_without_camera = calculate_min_camera_of_node(node.right)
                min_right = min(right_with_camera, right_without_camera)
                
                # 已经看出来这里有问题，比如对输入 [0,0,null,0,null,0,null,null,0] 来说。假定某个node的
                # 右孩子为空，此时 `left_without_camera + right_with_camera` 就不对了。
                # 因为本来指望right_with_camera情形下，node的右子树根节点的摄像头可以顺便监控node，
                # 所以左半边可以是left_without_camera的情形。但是现在其实右子树完全没有，所以左边不能用
                # left_without_camera的情形。
                node_without_camera = min(left_with_camera + right_with_camera, left_with_camera + right_without_camera, left_without_camera + right_with_camera)

                leftleft_without, leftright_without, rightleft_without, rightright_without = 0,0,0,0
                # if is_leaf(node.left) and is_leaf(node.right):
                #     node_with_camera = 1

                if node.left:
                    _ , leftleft_without = calculate_min_camera_of_node(node.left.left)
                    _ , leftright_without = calculate_min_camera_of_node(node.left.right)
                if node.right:
                    _ , rightleft_without = calculate_min_camera_of_node(node.right.left)
                    _ , rightright_without = calculate_min_camera_of_node(node.right.right)
                avail_min_left = min(min_left, leftleft_without + leftright_without)
                avail_min_right = min(min_right, rightleft_without + rightright_without)
                node_with_camera = 1 + avail_min_left + avail_min_right
                node.val = node_with_camera * 10000 + node_without_camera
        
        if not root:
            return 0
        dfs_and_dp(root)
        root_with, root_without = calculate_min_camera_of_node(root)
        print root
        return min(root_with, root_without)
              
"""
https://leetcode-cn.com/submissions/detail/110901468/

69 / 170 个通过测试用例
状态：解答错误

输入：
[0,0,null,0,null,0,null,null,0]
输出：
1
预期：
2
"""
