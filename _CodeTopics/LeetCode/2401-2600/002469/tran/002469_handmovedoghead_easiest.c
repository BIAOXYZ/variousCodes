/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize){
    double* res = (double*)malloc(sizeof(double) * 2);
    res[0] = celsius + 273.15;
    res[1] = celsius * 1.80 + 32.00;
    *returnSize = 2;
    return res;
}

/*
https://leetcode.cn/submissions/detail/415867838/

执行用时：
0 ms
, 在所有 C 提交中击败了
100.00%
的用户
内存消耗：
5.4 MB
, 在所有 C 提交中击败了
43.00%
的用户
通过测试用例：
74 / 74
*/
