
`530. 二叉搜索树的最小绝对差` https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
- > 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

`530. 二叉搜索树的最小绝对差` https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/solution/er-cha-sou-suo-shu-de-zui-xiao-jue-dui-chai-by-lee/
- [x] 方法一：中序遍历
- > 朴素的方法是经过一次中序遍历将值保存在一个数组中再进行遍历求解，我们也可以在中序遍历的过程中用 pre 变量保存前驱节点的值，这样即能边遍历边更新答案，不再需要显式创建数组来保存，需要注意的是 pre 的初始值需要设置成任意负数标记开头，下文代码中设置为 -1。
- > 二叉树的中序遍历有多种方式，包括递归、栈、Morris 遍历等，读者可选择自己最擅长的来实现。下文代码提供最普遍的递归方法来实现，其他遍历方法的介绍可以详细看「94. 二叉树的中序遍历」的题解，这里不再赘述。
