
`1178. 猜字谜` https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/solution/cai-zi-mi-by-leetcode-solution-345u/
- [x] 方法一：二进制状态压缩
- [ ] 方法二：字典树

【详尽注释】详解「朴素位运算」& 「哈希表位运算」，以完整的优化分析思路 ... https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/solution/xiang-jin-zhu-shi-xiang-jie-po-su-wei-yu-3cr2/
- > **位运算说明**
  * > `a >> b & 1` 代表检查 a 的第 b 位是否为 1，有两种可能性 0 或者 1
  * > `a += 1 << b` 代表将 a 的第 b 位设置为 1 (当第 b 位为 0 的时候适用)
  * > 如不想写对第 b 位为 0 的前置判断，`a += 1 << b` 也可以改成 `a |= 1 << b`
  * > PS. 1 的二进制就是最低位为 1，其他位为 0 哦
  * > 以上两个操作在位运算中出现频率超高，建议每位同学都加深理解。

「手画图解」巧用位运算，思路解析 | leetcode 1178 猜字谜 https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/solution/shou-hua-tu-jie-si-lu-jie-xi-leetcode-11-12dy/
- 评论：
  * > 学到了
    ```console
    a = mask = "eca" = 10101

    |  a - 1  |  a = (a - 1) & mask  |
    |  10100  |  10100  = "ec"       |
    |  10011  |  10001  = "ea"       |
    |  10000  |  10000  = "e"        |
    |  01111  |  00101  = "ca"       |
    |  00100  |  00100  = "c"        |
    |  00011  |  00001  = "a"        |
    |  00000  |  end                 |
    ```

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
    print "mask =", mask
print "final mask is:", mask
print "\n"

subset = mask
res = []
while subset:
    s = subset | (1 << (ord(puzzle[0]) - ord("a")))
    res.append(s)
    print res
    subset = (subset - 1) & mask
    print subset
print "final res is:", res
--------------------------------------------------
mask = 4
mask = 12
mask = 28
final mask is: 28


[30]
24
[30, 26]
20
[30, 26, 22]
16
[30, 26, 22, 18]
12
[30, 26, 22, 18, 14]
8
[30, 26, 22, 18, 14, 10]
4
[30, 26, 22, 18, 14, 10, 6]
0
final res is: [30, 26, 22, 18, 14, 10, 6]
```
