-- lists all records of the table second_table
-- rows without a name value are not listed
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
