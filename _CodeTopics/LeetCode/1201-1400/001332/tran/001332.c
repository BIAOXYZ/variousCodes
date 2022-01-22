#include <string.h>

bool is_palindrome(char* s) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        ++left;
        --right;
    }
    return true;
}

int removePalindromeSub(char * s){
    return is_palindrome(s) ? 1 : 2;
}

/*
https://leetcode-cn.com/submissions/detail/261292394/

执行用时：0 ms, 在所有 C 提交中击败了100.00%的用户
内存消耗：5.5 MB, 在所有 C 提交中击败了18.84%的用户
通过测试用例：
48 / 48
*/
