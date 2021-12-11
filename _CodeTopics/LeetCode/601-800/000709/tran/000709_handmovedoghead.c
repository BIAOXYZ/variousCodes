#include <ctype.h>
#include <string.h>

char * toLowerCase(char * s){
    int length = strlen(s);
    for (int i = 0; i < length; ++i) {
        s[i] = tolower(s[i]);
    }
    return s;
}

/*
https://leetcode-cn.com/submissions/detail/247606370/

执行用时：0 ms, 在所有 C 提交中击败了100.00%的用户
内存消耗：5.7 MB, 在所有 C 提交中击败了16.01%的用户
通过测试用例：
114 / 114
*/
