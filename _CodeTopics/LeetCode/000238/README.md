
```py
length = 3
for i in range(length-1,0,-1):
    print "i= ", i
for j in range(length-1,-1,-1):
    print "j= ", j
--------------------------------------------------
i=  2
i=  1
j=  2
j=  1
j=  0
```

```py
# 申请定长list的两种方法。在第181场周赛的笔记里也有记录
# https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode_contest/weekly/181/general.md

length = 5
left = [1]*length
right = [1 for i in range(length)]
print left
print right
--------------------------------------------------
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
```
