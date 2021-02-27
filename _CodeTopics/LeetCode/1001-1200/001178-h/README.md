
`1178. 猜字谜` https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/solution/cai-zi-mi-by-leetcode-solution-345u/
- [x] 方法一：二进制状态压缩
- [ ] 方法二：字典树

# 测试用例

```
["aaaa","asas","able","ability","actt","actor","access"]
["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
```

# 代码片段

位运算部分代码不好读，于是提出来部分，运行一下方便后面看。

```py
puzzle = 'bcde'
mask = 0
for i in range(1, 4):
    mask |= (1 << (ord(puzzle[i]) - ord("a")))
print mask
  
subset = mask
res = []
while subset:
    s = subset | (1 << (ord(puzzle[0]) - ord("a")))
    res.append(s)
    subset = (subset - 1) & mask
print res
--------------------------------------------------
28
[30, 26, 22, 18, 14, 10, 6]
```
