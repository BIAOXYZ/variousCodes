

# 笔记

## `000100_algo2.py`

`000100_algo2.py`里的那个“**用bfs依次获取所有节点的值并存在一个list中返回**”这个函数`return_all_nodes_bfs()`实现的还是有些问题，想复杂了。结果那个复杂的实现反而不对。我们以这样一颗树为例：
```
   1
  / \
 2    3
/ \  / \
        4
```
很明显，其节点按bfs顺序输出应该是`[1, 2, 3, null/None, null/None, null/None, 4]`

### // `000100_algo2.py` + 1行print语句
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def return_all_nodes_bfs(node):
            if not node:
                return []
            temp, res = [node], [node.val]
            while temp:
                currnode = temp.pop(0)
                if currnode == None:
                    continue
                if currnode.left == currnode.right == None:
                    continue
                elif currnode.left and not currnode.right:
                    temp.append(currnode.left)
                    temp.append(None)
                    res.append(currnode.left.val)
                    res.append(None)
                elif currnode.right and not currnode.left:
                    temp.append(None)
                    temp.append(currnode.right)
                    res.append(None)
                    res.append(currnode.right.val)
                else:
                    temp.append(currnode.left)
                    temp.append(currnode.right)
                    res.append(currnode.left.val)
                    res.append(currnode.right.val)
            if res[-1] == None:
                res.pop()
            print res
            return res

        return return_all_nodes_bfs(p) == return_all_nodes_bfs(q)
```

```console
输入
[1,2,3]
[1,2,3,null,null,null,4]

输出
false

预期结果
false

stdout
[1, 2, 3]
[1, 2, 3, None, 4]
```

【[:star:][`*`]】 这个实现少了两个`None`的原因就是`节点2`虽然没有孩子，但只要它的下一层不全是`None节点`并且非空子节点按顺序是在它的孩子右边的，那它的俩`None节点`孩子也不能省略。对比一下下面就更明白了：

### // 改进版的`000100_algo2.py`（但是这个没有.py文件对应，只是在leetcode系统里自己试了），主要是bfs遍历时往栈里加孩子节点那里不一样（这里更像`000100_algo2_optm.py`）。
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def return_all_nodes_bfs(node):
            if not node:
                return []
            temp, res = [node], [node.val]
            while temp:
                currnode = temp.pop(0)
                if currnode == None:
                    continue
                else:
                    temp.append(currnode.left)
                    temp.append(currnode.right)
                    res.append(currnode.left.val) if currnode.left else res.append(None)
                    res.append(currnode.right.val) if currnode.right else res.append(None)
            while res[-1] == None:
                res.pop()
            print res
            return res

        return return_all_nodes_bfs(p) == return_all_nodes_bfs(q)
```

```console
输入
[1,2,3]
[1,2,3,null,null,null,4]

输出
false

预期结果
false

stdout
[1, 2, 3]
[1, 2, 3, None, None, None, 4]
```

### // 上面那个代码再加一行print（主要是为了说明第二个while语句的作用：去掉所有末尾多余的None），同时输入也变了一点点：`节点4`变成了`节点3`的左孩子。

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def return_all_nodes_bfs(node):
            if not node:
                return []
            temp, res = [node], [node.val]
            while temp:
                currnode = temp.pop(0)
                if currnode == None:
                    continue
                else:
                    temp.append(currnode.left)
                    temp.append(currnode.right)
                    res.append(currnode.left.val) if currnode.left else res.append(None)
                    res.append(currnode.right.val) if currnode.right else res.append(None)
            print res
            while res[-1] == None:
                res.pop()
            print res
            return res

        return return_all_nodes_bfs(p) == return_all_nodes_bfs(q)
```

```console
输入
[1,2,3]
[1,2,3,null,null,4]

输出
false

预期结果
false

stdout
[1, 2, 3, None, None, None, None]
[1, 2, 3]
[1, 2, 3, None, None, 4, None, None, None]
[1, 2, 3, None, None, 4]
```
