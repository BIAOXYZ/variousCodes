
`114. 二叉树展开为链表` https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/

# 笔记

## `000114.py`

主要思想是通过观察发现可以通过每次把右孩子压到一个全局栈里，然后当相应的左孩子处理完了的时候，一个个pop出栈处理即可。比如如下输入，最开始会把`节点5`压栈，然后继续往下走，`节点4`也会入栈。等到`节点3`处理完了（所谓“处理完了”的标志是该节点为叶子结点，也就是其左右孩子均为None），此时栈顶的恰好是需要处理的`节点4`，然后依次类推即可。
```
    1
   / \
  2   5
 / \   \
3   4   6
```
