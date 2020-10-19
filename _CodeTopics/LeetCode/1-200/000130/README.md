
`130. 被围绕的区域` https://leetcode-cn.com/problems/surrounded-regions/solution/bei-wei-rao-de-qu-yu-by-leetcode-solution/
- 方法一：深度优先搜索
- [x] 方法二：广度优先搜索

bfs+递归dfs+非递归dfs+并查集 https://leetcode-cn.com/problems/surrounded-regions/solution/bfsdi-gui-dfsfei-di-gui-dfsbing-cha-ji-by-ac_pipe/

# 笔记

## `000130.py`

本来以为这个实现是广度优先遍历，因为觉得是**围绕某个坐标`[x,y]`周围一圈的四个点`[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]`层层遍历的**，所以里面遍历的那个函数名字也是`from_nochange_node_bfs()`。但是后来想了想这个其实是个深度优先遍历- -我的实现里，先把最外面四条边里值为`'O'`的节点取出来，并形成数组`noChangeNeed`这个操作也是让我搞错了的原因之一。。。因为这个动作太像BFS的过程了。但其实这个算法的实质还是DFS。
