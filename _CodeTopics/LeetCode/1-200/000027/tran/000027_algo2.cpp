class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        if (nums.size() == 0) {
            return 0;
        }
        // 注意，C++ vector中迭代器可能有失效的问题存在，所以跟python的倒序遍历删除不一样！
        // 写法的话就是注意:
        //   1. for 循环第三项不要搞 ++it，而是在循环体里搞。
        //   2. 需要用 erase 的返回结果给 it 赋值，代表被删除的迭代器 it 的后一个迭代器的值。
        //   3. 不是倒序遍历删除了，而是正序遍历删除。
        // 详情参见笔记吧。
        for (auto it = nums.begin(); it != nums.end(); ) {
            if (*it == val) {
                it = nums.erase(it);
            } else {
                ++it;
            }
        }
        return nums.size();
    }
};

/*
https://leetcode-cn.com/submissions/detail/169430482/

113 / 113 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 8.5 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：8.5 MB, 在所有 C++ 提交中击败了66.29%的用户
*/
