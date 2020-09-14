
`94. 二叉树的中序遍历` https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/
- [x] 方法一：递归
- [x] 方法二：栈
- 方法三：Morris 中序遍历

【[:star:][`*`]】 颜色标记法-一种通用且简明的树遍历方法 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
```console
其核心思想如下：
● 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
● 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
● 如果遇到的节点为灰色，则将节点的值输出。

使用这种方法实现的中序遍历如下：

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

如要实现前序、后序遍历，只需要调整左右子节点的入栈顺序即可。
```
- https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/204119

【[:star:][`*`]】 「手画图解」用栈模拟中序遍历，怎么做以及为什么 | 递归与迭代 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/shou-hua-tu-jie-yong-zhan-mo-ni-zhong-xu-bian-li-z/

二叉树的中序遍历 - 迭代法 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/die-dai-fa-by-jason-2/

彻底吃透二叉树的前中后序递归法和迭代法！！ https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/che-di-chi-tou-er-cha-shu-de-qian-zhong-hou-xu-d-2/

递归和非递归两种解法以及总结（最好的击败了100%的用户） https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/di-gui-he-fei-di-gui-liang-chong-jie-fa-by-sdwwld/

# `WA--000094_impl2.py`

- 【1】 为什么某些测试用例下，执行代码返回结果正确，但提交解答却出错了 https://support.leetcode-cn.com/hc/kb/article/1194344/
- 【2】 https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000104/000104_impl.py
```py
class Solution(object):
    maxdep = currdep = 0
```
- 【3】 https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000114/000114.py
```py
class Solution(object):
    rightChildrenStack = []
```

参考上面的链接，就知道为啥`WA--000094_impl2.py`错了——其实也没错，是leetcode对全局变量和类内变量（也就是类成员变量）支持太差了。

但是我比较奇怪的一点是：类似【2】的用法我以前也不止一次用，都能对的。如果说是因为【2】里面的类内变量`maxdep`或`currdep`都是普通变量，但是`WA--000094_impl2.py`里的类内变量`res`是个list。但是【3】里的`rightChildrenStack`也是list啊。。。回头再仔细分析下具体代码好了。
