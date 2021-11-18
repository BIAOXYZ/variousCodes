# Write your MySQL query statement below

SELECT player_id, MIN(event_date) AS "first_login" 
FROM Activity 
GROUP BY player_id; 

/*
https://leetcode-cn.com/submissions/detail/209707869/

12 / 12 个通过测试用例
状态：通过
执行用时: 1062 ms
内存消耗: 0 B

执行用时：1062 ms, 在所有 MySQL 提交中击败了5.01%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
*/
