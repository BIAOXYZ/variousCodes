
`剑指 Offer 20. 表示数值的字符串` https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/biao-shi-shu-zhi-de-zi-fu-chuan-by-leetcode-soluti/
- [x] 方法一：确定有限状态自动机
  * > 自动机驱动的编程，可以被看做一种暴力枚举方法的延伸：它穷尽了在任何一种情况下，对应任何的输入，需要做的事情。
  * > 自动机在计算机科学领域有着广泛的应用。在算法领域，它与大名鼎鼎的字符串查找算法「KMP」算法有着密切的关联；在工程领域，它是实现「正则表达式」的基础。
  * > 在 [C++ 文档](https://en.cppreference.com/w/cpp/language/floating_literal) 中，描述了一个合法的数值字符串应当具有的格式。具体而言，它包含以下部分：

面试题20. 表示数值的字符串（有限状态自动机，清晰图解） https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/

O（n）Python解题五法（逻辑判断，regex，dfa等）附加详细分析 https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/onpythonjie-ti-wu-fa-luo-ji-pan-duan-regexdfadeng-/

C++：模拟题（思路简单，逻辑清晰） https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/cmo-ni-ti-si-lu-jian-dan-luo-ji-qing-xi-by-xiaonen/

最简洁的Python解法！ https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/zui-jian-ji-de-pythonjie-fa-by-luyao777/

# `20.py`

- 这题有个毛线意思，纯粹是体力活。。。
- 开始也想到了状态`'START'`和`'blank-before'`应该是重复的，但是还是从大而全的角度都先定义了吧。然后等到写状态转移表的时候立刻就发现了果然是重复的。。。具体来说是指这里：
```py
            'START':{
                'BLANK':'blank-before',
                'DIGIT':'digit-before-dot',
                'DOT':'dot-without-num',
                'SIGN':'sign-for-num'
                },
            'blank-before':{
                'BLANK':'blank-before',
                'DIGIT':'digit-before-dot',
                'DOT':'dot-without-num',
                'SIGN':'sign-for-num'
            },
```
- 同理，拒绝状态其实也不用定义（可以看到代码里定义了也没用上），只要判断最后的状态是否在接受状态集 acceptState 里即可。
