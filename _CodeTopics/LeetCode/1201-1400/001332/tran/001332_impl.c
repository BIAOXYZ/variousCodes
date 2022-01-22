#include <string.h>

bool is_palindrome_v2(char* s) {
    int n = strlen(s);
    for (int i = 0; i < n/2; ++i) {
        if (s[i] != s[n-1-i]) {
            return false;
        }
    }
    return true;
}

int removePalindromeSub(char * s){
    return is_palindrome_v2(s) ? 1 : 2;
}

/*
https://leetcode-cn.com/submissions/detail/261294311/

执行用时：0 ms, 在所有 C 提交中击败了100.00%的用户
内存消耗：5.3 MB, 在所有 C 提交中击败了98.55%的用户
通过测试用例：
48 / 48
*/
/*
接近双百了。。。虽然并没有什么意义。
*/
