-- script that displays the average temperature in the file, temperatures.sql
-- by city ordered by temperature (descending)

SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
