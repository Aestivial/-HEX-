SELECT Weather.id 
FROM Weather JOIN Weather AS w 
WHERE Weather.temperature > w.temperature 
AND DATEDIFF(Weather.recordDate,w.recordDate)=1;