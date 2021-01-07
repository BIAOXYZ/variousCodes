// 草他妈打工人太他妈难了，干一天活头昏眼花，怎么都找不出错来。想多调试一会都不行，因为明天还得拿命换钱。我艹他妈。
class Solution {
public:
    void reverseList(vector<int>& l, int start, int end) {
        int length = end - start + 1;
        if (length == 1) {
            return;
        }
        else {
            for (int i = start; i < start + length/2 - 1; i++) {
                int tmp;
                tmp = l[i];
                l[i] = l[end-1-i];
                l[end-1-i] = tmp;
            }
        }
    }

    void rotate(vector<int>& nums, int k) {

        int length = nums.size();
        if (k >= length)
            k = k % length;
        if (k == 0 or length == 1)
            return;
        
        reverseList(nums, 0, length);
        for (auto elem : nums)
            cout << elem;
        cout << endl;
        reverseList(nums, 0, k);
        for (auto elem : nums)
            cout << elem;
        reverseList(nums, k, length);

    }
};

/*
https://leetcode-cn.com/submissions/detail/136804416/

9 / 35 个通过测试用例
状态：解答错误

输入：
[1,2,3,4,5,6,7]
3
输出：
[5,6,7,4,3,2,1]
预期：
[5,6,7,1,2,3,4]
*/
