# Write your MySQL query statement below

SELECT a.player_id, a.device_id from Activity a
WHERE (a.player_id, a.event_date) 
IN (
    SELECT player_id, MIN(event_date) AS "first_login" 
    FROM Activity 
    GROUP BY player_id
);

/*
https://leetcode-cn.com/submissions/detail/209733437/

12 / 12 个通过测试用例
状态：通过
执行用时: 335 ms
内存消耗: 0 B

执行用时：335 ms, 在所有 MySQL 提交中击败了100.00%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
*/
/*
又一个双百，不过可能只是因为是会员题目，做得人少吧。
*/
