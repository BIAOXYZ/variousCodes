# Write your MySQL query statement below

SELECT a1.player_id, a1.device_id
FROM activity AS a1
WHERE a1.event_date <= ALL (
	SELECT a2.event_date
	FROM activity AS a2
	WHERE a1.player_id = a2.player_id
);

/*
https://leetcode-cn.com/submissions/detail/209745694/

12 / 12 个通过测试用例
状态：通过
执行用时: 1463 ms
内存消耗: 0 B

执行用时：1463 ms, 在所有 MySQL 提交中击败了5.66%的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
*/
/*
和 `000512.sql` （也就是用 IN 实现的那个）比起来，速度差了很多，应该就是 ALL 的话都得查，过滤太少。
*/
