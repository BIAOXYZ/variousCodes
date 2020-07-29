
`329. 矩阵中的最长递增路径` https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/ju-zhen-zhong-de-zui-chang-di-zeng-lu-jing-by-le-2/
- 方法一：记忆化深度优先搜索
- 方法二：拓扑排序

几个问答看懂深度搜索+记忆化思路, 时间击败99% https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/ji-ge-wen-da-kan-dong-shen-du-sou-suo-ji-yi-hua-sh/

python3 深度优先搜索（记忆化+递归）+动态规划（排序） 详细过程 https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/python3-shen-du-you-xian-sou-suo-ji-yi-hua-di-gui-/

# 笔记

# 1. 官方答案`方法一`：

```py
class Solution:
    
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans
```

## 1.1 语法点：官方答案`方法一`里用到了python的装饰器，并且是带参数的（尽管参数是None）装饰器。

装饰器 https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
```py
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
--------------------------------------------------
call now():
2015-3-25
```

## 1.2 语法点：调用类内（类方法外）的成员变量`DIRS`时，除了用`self.DIRS`，还可以像官方答案一样用`Solution.DIRS`。

```py
for dx, dy in Solution.DIRS:
```

## 1.3 语法点：`DIRS`内部的元素是tuple时，可以用下面的两个一起遍历的语法；但是如果`DIRS`内部的元素是list时就不行。

```py
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for dx, dy in DIRS:
  print dx
  print dy
--------------------------------------------------
-1
0
1
0
0
-1
0
1
```

```py
DIRS2 = [[-1, 0], [1, 0], [0, -1], [0, 1]
for dx, dy in DIRS2:
  print dx
  print dy
--------------------------------------------------
  File "main.py", line 3
    for dx, dy in DIRS2:
      ^
SyntaxError: invalid syntax
```
