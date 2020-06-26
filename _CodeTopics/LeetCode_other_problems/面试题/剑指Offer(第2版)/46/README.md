
- 正确答案和错误答案只差了一个数字（是真的就一个数字），但是也不是笔误，就是第一次想错了。
- 总体而言没什么难度，就是递归。另外如果是用Solution类的函数递归得加上`self.`，好久没用python面向对象了，忘了好多。
- 看了[官方答案](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-by-leetcode-sol/)后我还在纳闷，为啥输入是1402时我的答案也是对的，按理说最后的02我的code也会处理成`0-2`和`2`两种情况啊。后来单步跟进去看了下，发现是python的`int()`对于`02`，结果直接就是`2`。所以属于碰巧躲过了个坑。
```
input：1402

第一轮：
num: 1402
numstr: '1402'
numstr[0:2]: '14'
numstr[2:]: '02'
numstr[1:]: '402'
由于`14 < 25`，然后会走`return self.translateNum(int(numstr[1:])) + self.translateNum(int(numstr[2:]))`，
也就是对'402'转成的整数和'02'转成的整数继续调用，首先是'402'转成的整数那个分支。

第二轮：
num: 402
numstr: '402'
numstr[0:2]: '40'
numstr[2:]: '2'
numstr[1:]: '02'
由于`40 > 25`，然后会走`return self.translateNum(int(numstr[1:]))`，
也就是对'02'转成的整数继续调用。

第三轮：
虽然是从'02'转成int类型，但是转完后直接就是2，自动把0就给去了。
num: 2
```
