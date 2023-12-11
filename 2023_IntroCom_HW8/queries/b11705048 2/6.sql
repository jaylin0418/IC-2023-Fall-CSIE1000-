-- 6. How many times for each character to visit his/her homeworld? show character names and times appeared in TimeTable. (Name, Times) 
SELECT C.Name, COUNT(T.Planet_Name) AS Times
FROM Characters C, TimeTable T
WHERE C.Name = T.Character_Name AND C.Homeworld =
T.Planet_Name
GROUP BY C.Name;