
`143. 重排链表` https://leetcode-cn.com/problems/reorder-list/solution/zhong-pai-lian-biao-by-leetcode-solution/
- [x] 方法一：线性表
- 方法二：寻找链表中点 + 链表逆序 + 合并链表
  * > 1.找到原链表的中点（参考「[876. 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/)」）。
    + > 我们可以使用快慢指针来 O(N) 地找到链表的中间节点。
  * > 2.将原链表的右半端反转（参考「[206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)」）。
    + > 我们可以使用迭代法实现链表的反转。
  * > 3.将原链表的两端合并。
    + > 因为两链表长度相差不超过 11，因此直接合并即可。
