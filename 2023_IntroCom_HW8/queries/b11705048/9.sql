-- 9. Find all characters that never visited any empire planets. (Name) 
SELECT DISTINCT C.Name
FROM characters C
WHERE C.Name NOT IN (SELECT DISTINCT T.Character_Name
                     FROM TimeTable T
                     WHERE T.Planet_Name IN (SELECT DISTINCT P.Name
                                             FROM planets P
                                             WHERE P.Affiliation = "empire"));