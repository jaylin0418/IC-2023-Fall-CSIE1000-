-- 3. Retrieve the names of characters who have visited more than one planet. (Character_Name)
-- SELECT DISTINCT T.Character_Name
-- FROM TimeTable T
-- WHERE (SELECT COUNT(DISTINCT T1.Planet_Name) FROM TimeTable T1 WHERE T1.Character_Name = T.Character_Name) > 1;
SELECT Character_Name
FROM TimeTable
GROUP BY Character_Name
HAVING COUNT(DISTINCT Planet_Name) > 1;