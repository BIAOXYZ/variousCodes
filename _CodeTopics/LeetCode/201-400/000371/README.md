
`371. 两整数之和` https://leetcode-cn.com/problems/sum-of-two-integers/solution/liang-zheng-shu-zhi-he-by-leetcode-solut-c1s3/
- [x] 方法一：位运算
  * > 可以发现，对于整数 a 和 b：
    + > 在不考虑进位的情况下，其无进位加法结果为 `a⊕b`。
    + > 而所有需要进位的位为 `a & b`，进位后的进位结果为 `(a & b) << 1`。

位运算详解以及在 Python 中需要的特殊处理 https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/

【每日一题】清晰易懂的三种解法(每个方法击败100%, 0ms), 含详细注释「玩转力扣」 https://leetcode-cn.com/problems/sum-of-two-integers/solution/leetcode-ac-yanglr-easy-to-understand-qi-iy6c/

# 测试用例

```
1
2
2
3
-1
1
```
