int prefixCount(char ** words, int wordsSize, char * pref){

    int res = 0;
    for (int i = 0; i < wordsSize; ++i) {
        if (strncmp(words[i], pref, strlen(pref)) == 0) {
            res++;
        }
    }
    return res;
}

/*
https://leetcode.cn/submissions/detail/393732254/

执行用时：
8 ms
, 在所有 C 提交中击败了
59.31%
的用户
内存消耗：
6.4 MB
, 在所有 C 提交中击败了
60.69%
的用户
通过测试用例：
95 / 95
*/
