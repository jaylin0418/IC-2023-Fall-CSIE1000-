-- 5. For Luke Skywalker, for each movie that Luke appears in, what is the planet that has the different affiliation with him and that he travels to for the longest length of time? (Movie, Planet_Name) 
SELECT ST.Movie, ST.Planet_Name
FROM (
SELECT Movie, Planet_Name, Time_of_Departure - Time_of_Arrival AS
Spent_Time
FROM TimeTable, Planets
WHERE Character_Name = 'Luke Skywalker'
AND Planet_Name = Name
AND Affiliation != 'rebels'
) ST
INNER JOIN (
SELECT Movie, Max(Time_of_Departure - Time_of_Arrival) AS
Spent_Time
FROM TimeTable, Planets
WHERE Character_Name = 'Luke Skywalker'
AND Planet_Name = Name
AND Affiliation != 'rebels'
GROUP BY Movie
) MST
ON ST.Movie = MST.Movie AND ST.Spent_Time = MST.Spent_Time;