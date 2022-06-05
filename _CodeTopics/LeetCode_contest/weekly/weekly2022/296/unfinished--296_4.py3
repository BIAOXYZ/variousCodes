# 不知道为什么，看到一半觉得就是双向链表。。。大概是上周的周赛还是双周赛第三题的影响？

class Node:
    def __init__(self, ch, pre=None, nxt=None):
        self.val = ch
        self.pre = pre
        self.nxt = nxt

class TextEditor:

    def __init__(self):
        dummyHead = Node('|')
        self.cursor = dummyHead

    def addText(self, text: str) -> None:
        n = len(text)
        cursor = self.cursor
        for i in range(n-1, -1, -1):
            ch = text[i]
            nd = Node(ch, None, cursor)
            cursor.pre = nd
            cursor = nd
        
        """
        # 至少插入基本是对的了，别的回头看吧，写麻了。。。
        cursor2 = self.cursor
        while cursor2:
            print(cursor2.val)
            cursor2 = cursor2.pre
        """

    def deleteText(self, k: int) -> int:
        res = 0
        cursor = self.cursor
        while cursor.pre:
            prepre = cursor.pre.pre
            cursor.pre = prepre
            prepre.nxt = cursor
            res += 1
        return res
    
    def cursorLeft(self, k: int) -> str:
        cursor = self.cursor
        while cursor and cursor.pre and k > 0:
            prepre = cursor.pre.pre
            nxtnxt = cursor.nxt
            pre = cursor.pre
            # 双向链表操作过程
            cursor.pre = prepre
            cursor.nxt = pre
            pre.pre = cursor
            pre.nxt = nxtnxt
            if prepre:
                prepre.nxt = cursor
            if nxtnxt:
                nxtnxt.pre = pre
            k -= 1
        self.cursor = cursor
        res = []
        while cursor and cursor.pre and len(res) < 10:
            cursor = cursor.pre
            res.append(cursor.val)
        return ''.join(res)

    def cursorRight(self, k: int) -> str:
        cursor = self.cursor
        while cursor and cursor.nxt and k > 0:
            prepre = cursor.pre
            nxtnxt = cursor.nxt.nxt
            nxt = cursor.nxt
            # 双向链表操作过程
            cursor.pre = nxt
            cursor.nxt = nxtnxt
            nxt.pre = prepre
            nxt.nxt = cursor
            if prepre:
                prepre.nxt = nxt
            if nxtnxt:
                nxtnxt.pre = cursor
            k -= 1
        self.cursor = cursor
        res = []
        while cursor and cursor.nxt and len(res) < 10:
            cursor = cursor.nxt
            res.append(cursor.val)
        return ''.join(res)
        
        
# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
