int search(int* nums, int numsSize, int target){

    // 和 C++ 版本几乎一样的，除了数组大小必须显示传入。
    // 但是其实感觉 nums 的访问还是用指针形式更能体现 C 语言。
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target)
            left = mid + 1;
        else if (nums[mid] > target)
            right = mid - 1;
        else
            return mid;
    }
    return -1;
}

/*
https://leetcode-cn.com/submissions/detail/215642128/

46 / 46 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 7 MB

执行用时：28 ms, 在所有 C 提交中击败了96.90%的用户
内存消耗：7 MB, 在所有 C 提交中击败了54.45%的用户
*/
