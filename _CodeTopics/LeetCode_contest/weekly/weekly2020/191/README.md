
# 2020.05.31

第 191 场周赛 https://leetcode-cn.com/contest/weekly-contest-191
- 5424. 数组中两元素的最大乘积 https://leetcode-cn.com/contest/weekly-contest-191/problems/maximum-product-of-two-elements-in-an-array/
- 5425. 切割后面积最大的蛋糕 https://leetcode-cn.com/contest/weekly-contest-191/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
- 5426. 重新规划路线 https://leetcode-cn.com/contest/weekly-contest-191/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
- 5427. 两个盒子中颜色不同的球数量相同的概率 https://leetcode-cn.com/contest/weekly-contest-191/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

# 笔记

## (1)

语法：`max()`函数参数为某个列表；list的`.index()`方法；list的`.pop()`方法。
```py
l=[1,2,3,4,5]
maxnum = max(l)
print maxnum
ind = l.index(maxnum)
print ind
l.pop(ind)
print l
--------------------------------------------------
5
4
[1, 2, 3, 4]
```

## (2)

语法：以后判断大小直接用max()好了，可以省一个if判断的代码；列表的`.sort()`方法。
```py
num1 = 1
num2 = 2
num1 = max(num1, num2)
print num1
print num2
--------------------------------------------------
2
2
```

## (3)

语法：字典的`.values()`方法遍历字典的key对应的键值；小函数getKey根据字典的键值返回对应的key；第一个TLE的程序用到了递归，其实写的还是凑合的，但是python在效率方面无人权；后面的algo2和algo3其实算法大方向是类似的，但是也是超时，没办法。
```py
# https://stackoverflow.com/questions/8214932/how-to-check-if-a-value-exists-in-a-dictionary-python

>>> d = {'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}
>>> 'one' in d.values()
True
```
```py
def getKey(dic, val):
    return [k for k, v in dic.items() if v == val]
```
