
`179. 最大数` https://leetcode-cn.com/problems/largest-number/solution/zui-da-shu-by-leetcode-solution-sid5/
- [x] 方法一：排序

# 测试用例

```
[10,2]
[3,30,34,5,9]
[1]
[10]

[34323,3432]

[0,0]
```

# 语法点

>> //notes：python的`sort`类方法使用自定义的比较函数时，在升序排列的情况下，第一个参数 `x` 大于第二个参数 `y` 时，应该返回 `1` 还是 `-1`？
>>> `1`

python 自定义排序函数 https://www.cnblogs.com/superxuezhazha/p/5718829.html
```py
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
l = [36, 5, 12, 9, 21]
print sorted([36, 5, 12, 9, 21], reversed_cmp)
print l
l.sort(reversed_cmp)
print l
--------------------------------------------------
[36, 21, 12, 9, 5]
[36, 5, 12, 9, 21]
[36, 21, 12, 9, 5]
```

Python3 自定义 sort() 的排序规则 https://blog.csdn.net/gongjianbo1992/article/details/107324871
- > 在 Python2 中，sort 和 sorted 可以通过关键字参数 `cmp` 指定排序规则，但在 Python3 中这个参数给去掉了：
  ```console
  Python2： list.sort(cmp=None, key=None, reverse=False)
  Python3： list.sort(key=None, reverse=False)
  ```
- > 根据 Python3 的文档： https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=sort#list.sort 可以使用 `functools.cmp_to_key()` 将 Python2 风格的 `cmp` 函数转换为 `key` 函数。
