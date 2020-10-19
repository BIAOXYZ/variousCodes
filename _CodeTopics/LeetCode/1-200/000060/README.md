
`60. 第k个排列` https://leetcode-cn.com/problems/permutation-sequence/solution/di-kge-pai-lie-by-leetcode-solution/
- 方法一：数学 + 缩小问题规模

# 

```
1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321
```

语法点：
- python "".join() 出错TypeError: sequence item 0: expected string, int found https://www.cnblogs.com/alaska1131/articles/3535195.html
```console
python中使用join连接list时出现类型错误的解决办法
 
例：
>>> ls = [1,2,3]
>>> print ','.join(ls)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected string, int found
 
解决办法对list中的元素进行类型转换到string
 
>>> print ','.join('%s' % id for id in ls)
1,2,3
```
- TypeError: sequence item 0: expected string, int found https://stackoverflow.com/questions/10880813/typeerror-sequence-item-0-expected-string-int-found
  * > string.join connects elements inside list of strings, not ints. Use this generator expression instead:
    ```py
    values = ','.join(str(v) for v in value_list)
    ```
