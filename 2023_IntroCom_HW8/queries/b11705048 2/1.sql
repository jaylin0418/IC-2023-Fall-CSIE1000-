-- 1. Find the names of characters affiliated with the rebels who have visited Tatooine. (Name) 
SELECT DISTINCT C.Name
FROM characters C
WHERE C.Affiliation = "rebels"
AND C.Name IN (SELECT DISTINCT T.Character_Name FROM TimeTable T WHERE T.Planet_Name = "Tatooine");