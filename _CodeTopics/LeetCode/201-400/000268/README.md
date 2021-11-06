
`268. 丢失的数字` https://leetcode-cn.com/problems/missing-number/solution/diu-shi-de-shu-zi-by-leetcode-solution-naow/
- [ ] 方法一：排序
- [x] 方法二：哈希集合
- [ ] 方法三：位运算
- [ ] 方法四：数学

【宫水三叶】一题五解 :「排序」&「计数」&「原地哈希」&「数学」&「异或」 https://leetcode-cn.com/problems/missing-number/solution/gong-shui-san-xie-yi-ti-wu-jie-pai-xu-ji-te3s/

# 测试用例

```
[3,0,1]
```

# 语法

- Python 中 `set` 类型的 `A.difference(B)` 方法。
- Python 中 `set` 类型的 `A.pop()` 方法，据说是会随机pop出集合中的一个元素（ https://www.programiz.com/python-programming/methods/set/pop ），但是我试了下 `s = set([1,2,3,4])` 时，pop的顺序永远是 1-2-3-4。不过无所谓了。
