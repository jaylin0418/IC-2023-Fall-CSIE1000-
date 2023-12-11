-- 8. Which planet(s) have not been visited by any characters in all movies? (Name) 
SELECT DISTINCT P.Name
From planets P
WHERE P.Name NOT IN (SELECT DISTINCT T.Planet_Name from TimeTable T);
