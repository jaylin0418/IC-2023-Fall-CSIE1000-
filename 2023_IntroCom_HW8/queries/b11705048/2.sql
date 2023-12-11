-- 2. List the planets visited by Darth Vader in chronological order based on the time of arrival. (Planet_Name)
SELECT T.Planet_Name
FROM TimeTable T
WHERE T.Character_Name = "Darth Vader"
ORDER BY T.Time_of_Arrival;