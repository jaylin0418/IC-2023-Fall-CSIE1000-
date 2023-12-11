-- 4. List the planets visited by Han Solo in Movie 1 and Movie 3. (Planet_Name) 
SELECT DISTINCT T.Planet_Name
FROM TimeTable T
WHERE T.Character_Name = "Han Solo" AND T.Movie IN (1,3);