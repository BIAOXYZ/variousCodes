#if 0

这里以一个二分查找函数为例来说明三路判定的用法，该函数判定在已排好序的数组 v 中
是否存在一个特定的值 x。这里 v 的元素必须以递增次序排列。如果 v 中存在 x，则函数返回 x
在 v 中的位置（介于 0 与 n-1 之间的一个数），否则返回 -1。
二分查找法首先将输入值 x 与数组 v 的中间元素进行比较。如果 x 小于中间值，那么集中
查找数组的前半部分，否则查找数组的后半部分。无论哪种情况，下一步都是将 x 与所选那一
半的中间元素进行比较。这种将查找范围一分为二的过程会一直持续到找到输入值或者查找范
围变空为止。

/* binsearch：在 v[0] <= v[1] <= … <= v[n-1] 中查找 x */
int binsearch(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n – 1;
    while (low <= high) {
        mid = (low+high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else    /* 找到匹配 */
            return mid;
    }
    return -1; /* 无匹配 */
}

此程序的主要判定操作是每一步中 x 是否小于、大于还是等于中间元素 v[mid]；这正是
else-if 所擅长的工作。

#endif // 0


/* binsearch：在 v[0] <= v[1] <= … <= v[n-1] 中查找 x */
int binsearch(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n – 1;
    while (low <= high) {
        mid = (low+high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else    /* 找到匹配 */
            return mid;
    }
    return -1; /* 无匹配 */
}

