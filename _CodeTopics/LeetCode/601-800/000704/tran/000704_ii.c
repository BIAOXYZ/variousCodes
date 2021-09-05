int search(int* nums, int numsSize, int target){

    // 这次用 *(nums + mid) 代替 nums[mid]
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        // 这里 left + right 就不用括号了，因为 + 号优先级高于 >>，本来就是想让加法先运算的。
        int mid = left + right >> 1;
        if (*(nums + mid) < target)
            left = mid + 1;
        else if (*(nums + mid) > target)
            right = mid - 1;
        else
            return mid;
    }
    return -1;
}

/*
https://leetcode-cn.com/submissions/detail/215642296/

46 / 46 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 6.8 MB

执行用时：32 ms, 在所有 C 提交中击败了78.49%的用户
内存消耗：6.8 MB, 在所有 C 提交中击败了96.84%的用户
*/
