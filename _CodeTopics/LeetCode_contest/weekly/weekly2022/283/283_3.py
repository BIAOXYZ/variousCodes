# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        
        dic = defaultdict(list)
        allValues = set()
        hasInDegree = set() 
        for ind, d in enumerate(descriptions):
            dic[d[0]].append(ind)
            allValues.add(d[0])
            allValues.add(d[1])
            hasInDegree.add(d[1])
        ##print dic, allValues, hasInDegree, allValues - hasInDegree
        
        rootValue = (allValues - hasInDegree).pop()
        root = TreeNode(rootValue)
        
        def construct_tree(node):
            if node.val not in dic:
                return None
            for ind in dic[node.val]:
                childval, leftorright = descriptions[ind][1], descriptions[ind][2]
                if leftorright == 1:
                    leftchild = TreeNode(childval)
                    node.left = leftchild
                    construct_tree(node.left)
                elif leftorright == 0:
                    rightchild = TreeNode(childval)
                    node.right = rightchild
                    construct_tree(node.right)
        
        construct_tree(root)
        return root
    
"""
https://leetcode-cn.com/submissions/detail/278114498/

85 / 85 个通过测试用例
状态：通过
执行用时: 956 ms
内存消耗: 39.6 MB
"""
