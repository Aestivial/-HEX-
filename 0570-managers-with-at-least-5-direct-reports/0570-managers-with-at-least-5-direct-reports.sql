SELECT name from Employee 
WHERE id IN 
(SELECT managerId from Employee GROUP BY managerId HAVING COUNT(managerId)>4);