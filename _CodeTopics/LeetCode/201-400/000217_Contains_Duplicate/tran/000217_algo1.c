struct htElement {
    int key;
    int val;
    UT_hash_handle hh;
};

/*
void add_elem(struct htElement* dic, int k, int v) {
    struct htElement* kvPair;
    kvPair = malloc(sizeof(struct htElement));
    kvPair->key = k;
    kvPair->val = v;
    HASH_ADD_INT(dic, key, kvPair);
}
struct htElement *find_elem(struct htElement* dic, int k) {
    struct htElement *kvPair;
    HASH_FIND_INT(dic, &k, kvPair);
    return kvPair;
}
*/

// 仿照了官方答案的版本，查找和插入的时候没有用到我前面写的那俩子函数。
// 所以问题应该出在那俩子函数或其调用部分。
bool containsDuplicate(int* nums, int numsSize){
    struct htElement* dic = NULL;
    for (int i = 0; i < numsSize; i++) {
        struct htElement *tmp;
        HASH_FIND_INT(dic, nums + i, tmp);
        if (tmp == NULL) {
            tmp = malloc(sizeof(struct htElement));
            tmp->key = nums[i];
            HASH_ADD_INT(dic, key, tmp);
        }
        else {
            return true;
        }
    }
    return false;
}

/*
https://leetcode-cn.com/submissions/detail/131518351/

18 / 18 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 16.3 MB

执行用时：56 ms, 在所有 C 提交中击败了14.81%的用户
内存消耗：16.3 MB, 在所有 C 提交中击败了7.14%的用户
*/
