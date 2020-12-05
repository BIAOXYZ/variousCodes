
`621. 任务调度器` https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode-solution-ur9w/
- 方法一：模拟
- [x] 方法二：构造

【任务调度器】C++ 桶子_配图理解 https://leetcode-cn.com/problems/task-scheduler/solution/tong-zi-by-popopop/

Python 详解 https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/

# 测试用例

```
["A","A","A","B","B","B"]
2
["A","A","A","B","B","B"]
0
["A","A","A","A","A","A","B","C","D","E","F","G"]
2
["X","X","X","Y","Y","Y","Y"]
2
["X","X","X","Y","Y","Y","Y"]
3
["C"]
2
```

# 语法点

## `TLE--000621.py `

二维list转一维list的函数：
```py
def flatten_2d_list(lis):
    return [elem for listElem in sortedLoopList for elem in listElem]
```

来自这里： 
- Python 二维列表与一维列表的互相转化 https://blog.csdn.net/Yolandera/article/details/82847022
```py
L = [[1,2,3], [5,8], [7,8,9]]
print([i for item in L for i in item])
----------
[1, 2, 3, 5, 8, 7, 8, 9]
```

此外这里也有：
- 如何把嵌套的python list转成一个一维的python list? - 知乎 https://www.zhihu.com/question/27010691
