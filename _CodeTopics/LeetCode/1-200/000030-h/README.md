
`30. 串联所有单词的子串` https://leetcode.cn/problems/substring-with-concatenation-of-all-words/solution/chuan-lian-suo-you-dan-ci-de-zi-chuan-by-244a/
- [x] 方法一：滑动窗口

```
"barfoothefoobarman"
["foo","bar"]
"wordgoodgoodgoodbestword"
["word","good","best","word"]
"barfoofoobarthefoobarman"
["bar","foo","the"]
```

# 语法点

1. Counter的 - 和 subtract 方法效果是不一样的。。。详情见这里吧： https://github.com/BIAOXYZ/myNotes/blob/bfc33e4b9e3ea1d067ed7be781737c6d3ac342b2/programming_notes/programming_languages/prog_lang_python/Python_packages/Data_Types/collections/Counter/README.md
```py
>>> from collections import Counter
>>> x = 'aabc'
>>> y = 'aaab'
>>> xx = Counter(x)
>>> yy = Counter(y)
>>> xx
Counter({'a': 2, 'b': 1, 'c': 1})
>>> yy
Counter({'a': 3, 'b': 1})
>>>
>>> xx - yy
Counter({'c': 1})
>>>
>>> yy - xx
Counter({'a': 1})
>>>
>>> xx.subtract(yy)
>>> xx
Counter({'c': 1, 'b': 0, 'a': -1})
>>>
```

2. 字典遍历中删除（其实不难，但是第一反应的写法是错的而已）。详情参见这个帖子：
- Python字典遍历删除特定值 https://blog.csdn.net/zhangyuexiang123/article/details/101581035
```py
#coding=utf-8
D={'Google':'www.google.com','Bairu':'www.baidu.com','Taobao':'www.taobao.com'}
for key,value in D.items():
    if value=='www.google.com':
        D.pop('Google')
    else:
        continue
print(D)
```
```console
错误指示如下：
RuntimeError: dictionary changed size during iteration

分析原因：
遍历时不能修改字典元素，即不能在迭代的时候添加或删除属性, 只能更改属性值. 
```
```py
#coding=utf-8
D={'Google':'www.google.com','Bairu':'www.baidu.com','Taobao':'www.taobao.com'}
for key in list(D.keys()):
    if D[key]=='www.google.com':
        del D[key]
        continue
print(D)
#输出：{'Bairu': 'www.baidu.com', 'Taobao': 'www.taobao.com'}
```
