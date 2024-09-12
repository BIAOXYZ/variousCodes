#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int maxNumOfMarkedIndices(int* nums, int numsSize){

    // https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/submissions/563984418

    if (numsSize == 1)
        return 0;
    
    int ptr_small = 0;
    int ptr_large = numsSize / 2 + (numsSize & 1);

    qsort(nums, numsSize, sizeof(int), cmp);
    int res = 0;
    while (ptr_large <= numsSize - 1) {
        if (nums[ptr_small] * 2 <= nums[ptr_large]) {
            res += 2;
            ptr_small++;
        }
        ptr_large++;
    }
    return res;
}

/*
https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/submissions/564221181

通过
零知识证明
零知识证明
提交于 2024.09.13 01:01

执行用时分布
143
ms
击败
76.19%

消耗内存分布
16.74
MB
击败
52.38%
*/
