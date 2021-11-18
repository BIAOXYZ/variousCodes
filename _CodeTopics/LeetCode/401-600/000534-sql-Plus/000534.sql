# Write your MySQL query statement below

SELECT t1.player_id, t1.event_date, SUM(t2.games_played) AS "games_played_so_far"
FROM Activity AS t1, Activity t2
WHERE t1.player_id = t2.player_id AND t1.event_date >= t2.event_date
GROUP BY t1.player_id, t1.event_date;

/*
https://leetcode-cn.com/submissions/detail/209768948/

12 / 12 个通过测试用例
状态：通过
执行用时: 722 ms
内存消耗: 0 B

执行用时：722 ms, 在所有 MySQL 提交中击败了16.49%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
*/
