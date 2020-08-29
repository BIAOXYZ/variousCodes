
# 笔记

## 语法点

What does n[::-1] means in Python? https://stackoverflow.com/questions/28535392/what-does-n-1-means-in-python

```py
s = 'abc de fgh'
print s[::-1]
print s.split()
print s.split(" ")
print s.split(".")

s = ['Geeks', 'for', 'Geeks']
print ''.join(s)
print ' '.join(s)
--------------------------------------------------
hgf ed cba
['abc', 'de', 'fgh']
['abc', 'de', 'fgh']
['abc de fgh']
GeeksforGeeks
Geeks for Geeks
```
