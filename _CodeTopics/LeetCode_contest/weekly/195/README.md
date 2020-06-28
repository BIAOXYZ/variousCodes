
# 2020.06.28

第 195 场周赛 https://leetcode-cn.com/contest/weekly-contest-195
- 5448. 判断路径是否相交 https://leetcode-cn.com/contest/weekly-contest-195/problems/path-crossing/
- 5449. 检查数组对是否可以被k整除 https://leetcode-cn.com/contest/weekly-contest-195/problems/check-if-array-pairs-are-divisible-by-k/
- 5450. 满足条件的子序列数目 https://leetcode-cn.com/contest/weekly-contest-195/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
- 5451. 满足不等式的最大值 https://leetcode-cn.com/contest/weekly-contest-195/problems/max-value-of-equation/

# 笔记

## (1)

没注意又踩了python可变量和不可变量的坑，不过调试阶段已经发现了。

## (2)

python list的remove方法一次只能移除一个元素，不想做循环的话，可以用子函数或者lambda表达式。

Remove all occurrences of a value from a list? https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list
- >
  ```py
  Python 3.x

  >>> x = [1,2,3,2,2,2,3,4]
  >>> list(filter((2).__ne__, x))
  [1, 3, 3, 4]

  or

  >>> x = [1,2,3,2,2,2,3,4]
  >>> list(filter(lambda a: a != 2, x))
  [1, 3, 3, 4]

  Python 2.x

  >>> x = [1,2,3,2,2,2,3,4]
  >>> filter(lambda a: a != 2, x)
  [1, 3, 3, 4]
  ```
- >
  ```py
  def remove_values_from_list(the_list, val):
     return [value for value in the_list if value != val]

  x = [1, 2, 3, 4, 2, 2, 3]
  x = remove_values_from_list(x, 2)
  print x
  # [1, 3, 4, 3]
  ```
- >
  ```py
  x = [1, 2, 3, 4, 2, 2, 3]
  x = [i for i in x if i != 2]
  print x

  y = [1, 2, 3, 4, 2, 2, 3]
  while 2 in y:
    y.remove(2)
  print y
  --------------------------------------------------
  [1, 3, 4, 3]
  [1, 3, 4, 3]
  ```

个人实战：
```py
arr = [0,1,0,2,3]
arr = filter(lambda x: x != 0, arr)
print arr
--------------------------------------------------
[1, 2, 3]
```
