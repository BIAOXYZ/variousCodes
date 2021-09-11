# Write your MySQL query statement below

SELECT t1.FirstName, t1.LastName, t2.City, t2.State
FROM Person AS t1 LEFT JOIN Address AS t2
ON t1.PersonId = t2.PersonId;

/*
https://leetcode-cn.com/submissions/detail/218062422/

7 / 7 个通过测试用例
状态：通过
执行用时: 363 ms
内存消耗: 0 B

执行用时：363 ms, 在所有 MySQL 提交中击败了49.85%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
*/
