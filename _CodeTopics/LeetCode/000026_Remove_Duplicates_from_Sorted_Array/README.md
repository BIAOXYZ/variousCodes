
Python的list循环遍历中，删除数据的正确方法 https://www.cnblogs.com/bananaplan/p/remove-listitem-while-iterating.html
- > 初学Python，遇到过这样的问题，在遍历list的时候，删除符合条件的数据，可是总是报异常，代码如下：
  ```py
  num_list = [1, 2, 3, 4, 5]
  print(num_list)
  for i in range(len(num_list)):
      if num_list[i] == 2:
          num_list.pop(i)
      else:
          print(num_list[i])
  print(num_list)
  --------------------------------------------------
  [1, 2, 3, 4, 5]
  1
  4
  5
  Traceback (most recent call last):
    File "main.py", line 5, in <module>
      if num_list[i] == 2:
  IndexError: list index out of range
  ```
- > 原因是在删除list中的元素后，list的实际长度变小了，但是循环次数没有减少，依然按照原来list的长度进行遍历，所以会造成索引溢出。于是我修改了代码如下：
  ```py
  num_list = [1, 2, 3, 4, 5]
  print(num_list)
  for i in range(len(num_list)):
      if i >= len(num_list):
          break
      if num_list[i] == 2:
          num_list.pop(i)
      else:
          print(num_list[i])
  print(num_list)
  --------------------------------------------------
  [1, 2, 3, 4, 5]
  1
  4
  5
  [1, 3, 4, 5]
  ```
- > 这回不会报异常了，虽然最后，list中的元素[2]确实被删除掉了，但是，在循环中的打印结果不对，少打印了[3]。
- > 思考了下，知道了原因，当符合条件，删除元素[2]之后，后面的元素全部往前移，于是[3, 4, 5]向前移动，那么元素[3]的索引，就变成了之前[2]的索引（现在[3]的下标索引变为1了），后面的元素以此类推。可是，下一次for循环的时候，是从下标索引2开始的，于是，取出了元素[4]，就把[3]漏掉了。
- > 把代码修改成如下，结果一样，丝毫没有改观：
  ```py
  num_list = [1, 2, 3, 4, 5]
  print(num_list)
  for item in num_list:
      if item == 2:
          num_list.remove(item)
      else:
          print(item)
  print(num_list)
  --------------------------------------------------
  [1, 2, 3, 4, 5]
  1
  4
  5
  [1, 3, 4, 5]
  ```
- > 既然知道了问题的根本原因所在，想要找到正确的方法，也并不难，于是我写了如下的代码：
  ```py
  num_list = [1, 2, 3, 4, 5]
  print(num_list)
  i = 0
  while i < len(num_list):
      if num_list[i] == 2:
          num_list.pop(i)
          i -= 1
      else:
          print(num_list[i])
      i += 1
  print(num_list)
  --------------------------------------------------
  [1, 2, 3, 4, 5]
  1
  3
  4
  5
  [1, 3, 4, 5]
  ```
- > 我的做法是，既然用for循环不行，那就换个思路，用while循环来搞定。每次while循环的时候，都会去检查list的长度（i < len(num_list)），这样，就避免了索引溢出，然后，在符合条件，删除元素[2]之后，手动把当前下标索引-1，以使下一次循环的时候，通过-1后的下标索引取出来的元素是[3]，而不是略过[3]。

Python语法糖——遍历列表时删除元素 https://segmentfault.com/a/1190000007214571

Python如何一边遍历列表一边删除数据 https://www.jianshu.com/p/1547fdf962e4
