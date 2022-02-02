char * reversePrefix(char * word, char ch){
    
    char *p1 = word;
    char *p2 = strchr(word, ch);
    if (p2 != NULL) {
        while (p1 < p2) {
            char tmp = *p1;
            *p1 = *p2;
            *p2 = tmp;
            ++p1;
            --p2;
        }
    }
    return word;
}

/*
https://leetcode-cn.com/submissions/detail/264306117/

执行用时：0 ms, 在所有 C 提交中击败了100.00%的用户
内存消耗：5.7 MB, 在所有 C 提交中击败了18.24%的用户
通过测试用例：
112 / 112
*/
