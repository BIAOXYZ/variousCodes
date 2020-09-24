
`968. 监控二叉树` https://leetcode-cn.com/problems/binary-tree-cameras/solution/jian-kong-er-cha-shu-by-leetcode-solution/
- [x] 方法一：递归

# `000968_ugly.py`

主要思想和官方答案的类似（我估计和其他答案也差不多，但是大家的具体实现还是有差别的）。在分析时，我们focus到树中任意一个普通的节点`node`，为了满足以`node`为根节点的子树的所有节点能被监控覆盖，我们可以分成两种情况：
- **1.`node`节点上没有摄像头时，覆盖该子树需要的最小摄像头数目，在代码中记为`node_without_camera`**；
- **2.`node`节点上有摄像头时，覆盖该子树需要的最小摄像头数目，在代码中记为`node_with_camera`**。

对于第一种情况，由于`node`上没有摄像头，那么要求`node.left`和`node.right`除了自身被监控覆盖外，这两者中至少有一个上面得有摄像头——有没有可能左右两个孩子都需要有摄像头才能到达最小呢，也是可能的，看下面这棵树：如果`root`没有摄像头，左右孩子都有的话，需要的最小摄像头数目是二；否则只有左孩子有的话，右子树最下面的两个叶子都得有，此时最小摄像头数目是三了。
```
   o 
  / \
o     o
     /  \
   o     o
```
那么这种情况下基本的递推公式是：<br> `node_without_camera = min(left_with_camera + right_with_camera, left_with_camera + right_without_camera, left_without_camera + right_with_camera)`。看起来也很直观，但可惜只有上面这部分是不对的。`deliberate-WA--000968.py`也就是错在这里。
