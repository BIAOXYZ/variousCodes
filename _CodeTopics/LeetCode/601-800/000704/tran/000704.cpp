class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int length = nums.size();
        int left = 0, right = length - 1;
        while (left <= right) {
            // 注意运算符优先级，这里 ((right - left) >> 1) 最外层括号不能省- -
            int mid = left + ((right - left) >> 1);
            if (nums[mid] < target)
                left = mid + 1;
            else if (nums[mid] > target)
                right = mid - 1;
            else
                return mid;
        }
        return -1;
    }
};

/*
https://leetcode-cn.com/submissions/detail/215641472/

46 / 46 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 26.9 MB

执行用时：28 ms, 在所有 C++ 提交中击败了89.11%的用户
内存消耗：26.9 MB, 在所有 C++ 提交中击败了56.53%的用户
*/
