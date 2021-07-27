# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        def calculate_distance_from_string(s1, s2):
            len1, len2 = len(s1), len(s2)
            for i in range(min(len1, len2)):
                if s1[i] != s2[i]:
                    return len1 - i + len2 - i
            return abs(len1 - len2)

        dic = {root.val:'m'}
        def dfs_and_form_prefix_dic(node, currPrefix):
            if node.left:
                dic[node.left.val] = currPrefix + 'l'
                dfs_and_form_prefix_dic(node.left, currPrefix + 'l')
            if node.right:
                dic[node.right.val] = currPrefix + 'r'
                dfs_and_form_prefix_dic(node.right, currPrefix + 'r')
        
        dfs_and_form_prefix_dic(root, 'm')
        res = []
        for key, val in dic.items():
            if calculate_distance_from_string(dic[target.val], val) == k:
                res.append(key)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/200526742/

57 / 57 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.6 MB

执行用时：24 ms, 在所有 Python 提交中击败了71.43%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了26.53%的用户
"""
