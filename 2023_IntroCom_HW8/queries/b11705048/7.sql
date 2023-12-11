-- 7. List the names of characters who haven't made an appearance in any movie. (Name) 
SELECT C.Name
FROM characters C
WHERE C.Name NOT IN (SELECT DISTINCT T.Character_Name from TimeTable T);