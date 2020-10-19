
`116. 填充每个节点的下一个右侧节点指针` https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
- [x] 方法一：层次遍历
- [x] 方法二：使用已建立的 next 指针

「手画图解」DFS 递归 | 易于理解 https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/shou-hua-tu-jie-dfs-di-gui-yi-yu-li-jie-by-xiao_be/

BFS和递归共4种方式解决（最后3种击败了100%的用户） https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/bfshe-di-gui-zui-hou-liang-chong-ji-bai-liao-100-2/
- > 3，递归方式
  ```java
      public Node connect(Node root) {
          dfs(root, null);
          return root;
      }

      private void dfs(Node curr, Node next) {
          if (curr == null)
              return;
          curr.next = next;
          dfs(curr.left, curr.right);
          dfs(curr.right, curr.next == null ? null : curr.next.left);
      }
  ```

BFS、DFS、还有模拟递归 https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/bfs-dfs-huan-you-mo-ni-di-gui-by-suo-yi-ta-xi-huan/
- > `struct Node** q = (struct Node**)malloc(sizeof(struct Node*) * 5001);`

# 测试用例

这个题（以及之前的`LC117`）每次开始测试的时候都会加上`[]`，然后有问题，并且其他用例都过了。于是就会认为`[]`不是合法的输入，然后提交。最后直接RE。。。（在之前的`LC117`已经发生过了。。。不过稍有点不一样）
```console
[1,2,3,4,5,6,7]
[]
[1]
[1,2,3]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
```
