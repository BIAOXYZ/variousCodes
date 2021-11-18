# Write your MySQL query statement below

SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id; 

/*
https://leetcode-cn.com/submissions/detail/209698088/

12 / 12 个通过测试用例
状态：通过
执行用时: 547 ms
内存消耗: 0 B

执行用时：547 ms, 在所有 MySQL 提交中击败了13.08%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
*/
