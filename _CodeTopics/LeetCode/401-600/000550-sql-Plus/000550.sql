# Write your MySQL query statement below

SELECT
	ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS "fraction"
FROM
    Activity AS a
INNER JOIN (
	SELECT
		player_id, MIN(event_date) AS "first_login"
	FROM
		Activity
	GROUP BY 
		player_id
	) AS b
ON a.player_id = b.player_id AND DATEDIFF(a.event_date, b.first_login) = 1;

/*
https://leetcode-cn.com/submissions/detail/209783222/

12 / 12 个通过测试用例
状态：通过
执行用时: 467 ms
内存消耗: 0 B

执行用时：467 ms, 在所有 MySQL 提交中击败了59.60%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
*/
