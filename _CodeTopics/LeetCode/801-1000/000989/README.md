
`989. 数组形式的整数加法` https://leetcode-cn.com/problems/add-to-array-form-of-integer/solution/shu-zu-xing-shi-de-zheng-shu-jia-fa-by-l-jljp/
- 方法一：逐位相加

# 测试用例

```
[1,2,0,0]
34
[2,7,4]
181
[2,1,5]
806
[9,9,9,9,9,9,9,9,9,9]
1
```

# 语法点

```py
l = [1,2,3]
num = int(''.join([str(elem) for elem in l]))
print num, type(num)

num = 456
print [int(elem) for elem in list(str(num))]

A = [7,8]
print map(str, A)

print list(str(99))

x = map(int, "123")
print x, type(x[0])
y = list(map(int, "123"))
print y, type(y[0])
print x == y
--------------------------------------------------
123 <type 'int'>
[4, 5, 6]
['7', '8']
['9', '9']
[1, 2, 3] <type 'int'>
[1, 2, 3] <type 'int'>
True
```
