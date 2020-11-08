# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
这里之所以用官方代码再提交一遍，主要是因为那个`self.ans = 1`——所以python2因为没有nonlocal
类型的变量，要想在嵌套函数里用更高一层的变量看来只能这么搞：加 self. 从而变成类成员变量。。。
"""
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L+R+1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
        
"""
https://leetcode-cn.com/submissions/detail/121919811/

106 / 106 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 15.8 MB

执行用时：40 ms, 在所有 Python 提交中击败了32.55%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了6.52%的用户
"""
"""
结果看了官方答案后发现：
  第一我前面那个实现 `000543_ugly.py` 也没有多丑（因为官方也没有什么更好的算法或实现）；
  第二官方的速度还没我的快呢。。。
不过之所以要把官方答案再提交一下的原因前面注释里说了：
  看来python2对于非list，dict，set，tuple之类的变量，只能是用丑陋的self.xxx的形式。。。
"""
