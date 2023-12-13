-- MySQL server
-- should lists all records of the table second_table
-- should not list rows without a name value
-- should display the score and the name in the result
-- should be listed by descending score
-- should the database name will be passed as an argument

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;