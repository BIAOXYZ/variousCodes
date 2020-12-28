
# 2020.05.03

第 187 场周赛 https://leetcode-cn.com/contest/weekly-contest-187
- 5400. 旅行终点站 https://leetcode-cn.com/contest/weekly-contest-187/problems/destination-city/
- 5401. 是否所有 1 都至少相隔 k 个元素 https://leetcode-cn.com/contest/weekly-contest-187/problems/check-if-all-1s-are-at-least-length-k-places-away/
- 5402. 绝对差不超过限制的最长连续子数组 https://leetcode-cn.com/contest/weekly-contest-187/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
- 5403. 有序矩阵中的第 k 个最小数组和 https://leetcode-cn.com/contest/weekly-contest-187/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

# 笔记

## (1)

```py
# python字典类型变量的 .has_key() 方法。
if resdic.has_key(path[1]) is False:

# python字典添加新元素时直接用赋值。
resdic[path[1]] = 1

# python字典的 .items() 遍历方法。
for k, v in resdic.items():
```

## (3)

1. 程序本身应该是对的，但是又是坑爹的超时，没办法，python就是时间吃亏。
2. 另外这次对**跳出多重循环**有了一个更清晰的经验——以前当然也能写对，但是老是没注意就迷一下，然后耽误不少时间。这次通过下面这段代码片段就明白了：**你想跳出哪层循环，`if引导的flag判断和break语句`就在哪层循环的内部**。
```py
for j in range(i+1,length):
    flag = True
    for k in range(i,j):
        if abs(nums[j] - nums[k]) <= limit:
            continue
        else:
            flag = False
            break
    # 这里直接跳出第二层for循环。仔细看看想想就明白：
    # 在哪个for循环内部执行的逻辑里进行break，就跳出哪个for循环！
    # 所以上面那个break是跳出第三层for循环，而这个是跳出第二层for循环。
    if flag == False:
        break
```
如何在Python中使用break跳出多层循环？ - 知乎-李俊达的回答 - 知乎 https://www.zhihu.com/question/37076998/answer/144446959
> 利用全局变量，这样就算3个for或者4个for都是一样的
>> ![](https://pic3.zhimg.com/80/v2-216988ede7643b5ed670e590b3172cee_1440w.jpg)
