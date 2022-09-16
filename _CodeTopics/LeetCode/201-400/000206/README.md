
`206. 反转链表` https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode/
- [x] 方法一：迭代
- [x] 方法二：递归
- 回复：
  * https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode/334086
    ```console
    在其他评论区看到的，写得很清楚，Hope it helps!

    reverseList: head=1
        reverseList: head=2
            reverseList: head=3
                reverseList:head=4
                    reverseList:head=5 
                        终止返回
                    cur = 5
                    4.next.next->4，即5->4
                cur=5
                3.next.next->3，即4->3
            cur = 5
            2.next.next->2，即3->2
        cur = 5
        1.next.next->1，即2->1

        最后返回cur
    ```

动画演示+多种解法 206. 反转链表 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
- 回复：
  * https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/178642
  * https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/222187

```console
[1,2,3,4,5]
[]
[1]
[1,2]
[1,2,3]
[1,2,3,4]
```

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
