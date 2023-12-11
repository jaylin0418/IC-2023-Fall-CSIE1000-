-- 10. For each movie, which character(s) visited the highest number of planets? (Movie, Character_Name)
SELECT PCT.Movie, PCT.Character_Name
FROM (
SELECT Movie, Character_Name, COUNT(Planet_Name) AS
Planet_Count
FROM TimeTable
GROUP BY Movie, Character_Name
) PCT
INNER JOIN (
SELECT Movie, MAX(Planet_Count) AS Max_Planet_Count
FROM (
SELECT Movie, Character_Name, COUNT(Planet_Name) AS
Planet_Count
FROM TimeTable
GROUP BY Movie, Character_Name
) _
GROUP BY Movie
) MPCT
ON PCT.Movie = MPCT.Movie AND PCT.Planet_Count =
MPCT.Max_Planet_Count;