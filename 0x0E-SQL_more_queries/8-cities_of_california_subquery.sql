-- lists all the cities od California that are in the database hbtn_0d_usa
SELECT `id`, `name` FROM `cities`
WHERE `state_id` = (
	SELECT `id` FROM `states`
	WHERE `name` = 'California');
