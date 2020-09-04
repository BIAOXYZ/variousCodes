
`206. 反转链表` https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode/
- [x] 方法一：迭代
- [x] 方法二：递归

动画演示+多种解法 206. 反转链表 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/

# `000206.py` 和 `000206_optm.py`

首先附上官方答案的Java版本：
```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}
```

- `000206.py`总体思路以及实现都和答案是一样的，但是在处理head的时候显得啰嗦了。答案这种通过把第一个`pre`节点赋值为空节点的方式，使得代码简洁了不少。
- 然后又写的`000206_optm.py`就和答案可以说是一样的了。
