
`12. 整数转罗马数字` https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcod-75rs/
- 方法一：模拟
- 方法二：硬编码数字

# 测试用例

```
1
2
3
563
4
9
40
90
400
900

1994
1004
1404
14
```

# `000012.py`

就是通过一个用例 1994，来说明为啥还得有下面这个分支。
```py
                    if len(res) > 2 and res[-3] == res[-1]:
                        res = res[:-3] + letters[i] + letters[i-2]
```

仅看前六个字母`MDCCCC`就知道了：首先有四个`C`了，肯定要改写成`CD`，于是前六个变成`MDCD`。此时还不一定完，还需要用上面的if分支处理下，直到变成`MCM`才算正确。
```console
输入
1994
输出
"MDCCCCLXXXXIIII"
预期结果
"MCMXCIV"
```

官方答案两个实现也都没用到这种思路，所以还算是有点巧的。不过答案的实现更好写。。。
