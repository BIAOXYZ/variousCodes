
注：纯二分查找的实现请参见`LC704 二分查找`。

`35. 搜索插入位置` https://leetcode-cn.com/problems/search-insert-position/solution/sou-suo-cha-ru-wei-zhi-by-leetcode-solution/
- [x] 方法一：二分查找
  * > 官方答案C版本：
    ```c
    int searchInsert(int* nums, int numsSize, int target) {
        int left = 0, right = numsSize - 1, ans = numsSize;
        while (left <= right) {
            int mid = ((right - left) >> 1) + left;
            if (target <= nums[mid]) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
    ```
  * > 官方答案C++版本：
    ```c++
    class Solution {
    public:
        int searchInsert(vector<int>& nums, int target) {
            int n = nums.size();
            int left = 0, right = n - 1, ans = n;
            while (left <= right) {
                int mid = ((right - left) >> 1) + left;
                if (target <= nums[mid]) {
                    ans = mid;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            return ans;
        }
    };
    ```

35. 搜索插入位置（暴力、二分、STL及其自己实现） https://leetcode-cn.com/problems/search-insert-position/solution/35-sou-suo-cha-ru-wei-zhi-by-sunny_smile/
