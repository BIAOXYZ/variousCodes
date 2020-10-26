
`144. 二叉树的前序遍历` https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
- [x] 方法一：递归
- [x] 方法二：迭代
- 方法三：Morris 遍历

史上最全遍历二叉树详解 https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/leetcodesuan-fa-xiu-lian-dong-hua-yan-shi-xbian-2/

彻底吃透前中后序递归法（递归三部曲）和迭代法（不统一写法与统一写法） https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/dai-ma-sui-xiang-lu-chi-tou-qian-zhong-hou-xu-de-d/

# 测试用例

```
[1,2,3,4,5,6,7]
[1,null,2,3] 
[]
[1]
[1,2]
[1,2,3]
[1,2,3,4,null,5,6,null,7,null,8]
```

# `000144_algo2.py`

二叉树非递归形式的前序遍历，其实质是：
```
- 用一个栈，从当前节点（最开始时当然是根节点）开始，先把当前节点的val贴进结果集合里。
- 每次循环中如果当前节点的右孩子不空，就直接把右孩子push进栈里。
- 每次循环中如果当前节点的左孩子不空，就把左孩子设成下一个当前节点；如果左孩子空，开始把栈顶的有孩子节点pop出来作为当前节点。
```
