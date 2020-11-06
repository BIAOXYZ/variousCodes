/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* bit;

int count_one(int x) {
    int res = 0;
    while (x) {
        res += x % 2;
        x >>= 1;
    }
    return res;
}

int cmp(void* _x, void* _y) {
    int x = *(int*)_x, y = *(int*)_y;
    return bit[x] == bit[y] ? x - y : bit[x] - bit[y];
}

int* sortByBits(int* arr, int arrSize, int* returnSize) {
    // printf ("arrSize is: %d", arrSize);
    bit = malloc(sizeof(int) * 10001);
    memset(bit, 0, sizeof(int) * 10001);
    for (int i = 0; i < arrSize; ++i) {
        bit[arr[i]] = count_one(arr[i]);
    }
    /*
    for (int i = 0; i < arrSize; i++) {
        printf("%d, %d\n", arr[i], bit[i]);
    }
    */
    qsort(arr, arrSize, sizeof(int), cmp);
    free(bit);
    *returnSize = arrSize;
    return arr;
}

"""
https://leetcode-cn.com/submissions/detail/121437199/

77 / 77 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 11.5 MB

执行用时：24 ms, 在所有 C 提交中击败了95.15%的用户
内存消耗：11.5 MB, 在所有 C 提交中击败了5.45%的用户
"""
