
# 2020.05.30

第 27 场双周赛 https://leetcode-cn.com/contest/biweekly-contest-27
- 5408. 通过翻转子数组使两个数组相等 https://leetcode-cn.com/contest/biweekly-contest-27/problems/make-two-arrays-equal-by-reversing-sub-arrays/
- 5409. 检查一个字符串是否包含所有长度为 K 的二进制子串 https://leetcode-cn.com/contest/biweekly-contest-27/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
- 5410. 课程安排 IV https://leetcode-cn.com/contest/biweekly-contest-27/problems/course-schedule-iv/
- 5411. 摘樱桃 II https://leetcode-cn.com/contest/biweekly-contest-27/problems/cherry-pickup-ii/

# 笔记

## (1)

本来并不想用排序，后来想想排序还是快。所以先用了python列表的sort方法。注意，这个是直接把列表内容就改了，不是申请一个副本再排序。
- Python List sort()方法 https://www.runoob.com/python/att-list-sort.html
```py
aList = [123, 'Google', 'Runoob', 'Taobao', 'Facebook'];
aList.sort();
print "List : ", aList
--------------------------------------------------
List :  [123, 'Facebook', 'Google', 'Runoob', 'Taobao']
```

第二种方法里用到了cmp函数，这个比较两个字典的时候返回的不是bool类型，而是0，1，-1。所以最后要再判断下。
- Python 字典(Dictionary) cmp()方法 https://www.runoob.com/python/att-dictionary-cmp.html
```py
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)
--------------------------------------------------
Return Value : -1
Return Value : 1
Return Value : 0
```

### 易错点

注意：两个不同的字典初始化时不要图省事写成类似 `dic_a = dic_t = {}` 的形式，这样其实是一个字典，参见`27_1_algo2.py`。进一步参考python的可变对象和不可变对象。

## (2)

```py
s = '101'
print int(s)
print int(s,2)
print int(s,16)
--------------------------------------------------
101
5
257
```

// 然后第二题我第一种用字典的算法都过了，想着换成list再来一次吧（不过最后比较是通过对list元素求和），结果竟然WA了。。。算了，估计也不会再看了。
