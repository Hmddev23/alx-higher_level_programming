-- list all records of the second_table without the name
SELECT score, name FROM second_table WHERE NOT name='' ORDER BY score DESC;
