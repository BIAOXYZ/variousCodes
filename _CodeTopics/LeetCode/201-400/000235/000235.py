# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        """
        1.
        # 这个变量本来打算剪枝用的，但是好像剪枝也不太有多好的效果。比如 p = 2, q = 4 时，
        # 第一次剪枝了，第二次还得重新开始。所以这里暂不考虑剪枝了，先写完再说了。
        # twoKeyFound = 0
        
        2.
        # 写完了发现可能这个能直接利用二叉树的性质，一层层根据node的值二分来找。回头写写看吧。
        """

        dic = {}
        stack = [root]
        while stack:
            node = stack.pop(0)
            for child in [node.left, node.right]:
                if child:
                    stack.append(child)
                    dic[child.val] = node.val
        
        listp, listq = [p.val], [q.val]
        while listp[-1] != root.val:
            listp.append(dic[listp[-1]])
        while listq[-1] != root.val:
            listq.append(dic[listq[-1]])
        print "listp is %r, list q is %r" % (listp, listq)
        
        x = min(len(listp),len(listq))
        for i in range(-1, -x-1, -1):
            if listp[i] != listq[i]:
                return TreeNode(listp[i+1])
        
        # 这里漏了一种情况，比如 listp = [2,6], listq = [4,2,6]。如果在循环里都没有return回去，
        # 那说明较短的list的第一个数，也就是for循环完成后最后那个i，对于的就是答案。
        return TreeNode(listp[i])
        
"""
https://leetcode-cn.com/submissions/detail/111885179/

27 / 27 个通过测试用例
状态：通过
执行用时: 100 ms
内存消耗: 20.9 MB

执行用时：100 ms, 在所有 Python 提交中击败了5.10%的用户
内存消耗：20.9 MB, 在所有 Python 提交中击败了5.26%的用户
"""
