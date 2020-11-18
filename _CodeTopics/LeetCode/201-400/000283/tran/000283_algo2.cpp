class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int length = nums.size();
        int currPos = 0, currNonzeroPos = 0;

        for ( ; currPos < length; currPos++) {
            if (nums[currPos] != 0) {
                nums[currNonzeroPos] = nums[currPos];
                currNonzeroPos++;
            }
        }
        for (int i = currNonzeroPos; i < length; i++) {
            nums[i] = 0;
        }
    }   
};

/*
https://leetcode-cn.com/submissions/detail/124532999/

21 / 21 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 9.2 MB

执行用时：8 ms, 在所有 C++ 提交中击败了91.05%的用户
内存消耗：9.2 MB, 在所有 C++ 提交中击败了18.74%的用户
*/
