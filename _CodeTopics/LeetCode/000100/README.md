

# 笔记

## `000100_algo2.py`

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

