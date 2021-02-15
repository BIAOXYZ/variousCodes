
`695. 岛屿的最大面积` https://leetcode-cn.com/problems/max-area-of-island/solution/dao-yu-de-zui-da-mian-ji-by-leetcode-solution/
- [x] 方法一：深度优先搜索
- [x] 方法二：深度优先搜索 + 栈
- [x] 方法三：广度优先搜索

# 测试用例

```
[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
[[0,0,0,0,0,0,0,0]]
[[1,1,1],[1,1,0],[0,1,1]]
[[1,1,1],[0,1,1],[1,0,1]]
[[0]]
[[1]]
```

# `000695.py`

`is_legal_coordinate()`函数的新版本`is_legal_coordinate_v2()`——明显更简单好写，并且有可能效率还更高。

# `000695_algo3.py`

`000695_algo3.py` 和 `000695_algo2.py` 在形式上几乎是一模一样的，但是确实一个是`DFS+栈`，一个是`BFS`。除了函数名，唯一的区别就是`pop()`和`pop(0)`了。
