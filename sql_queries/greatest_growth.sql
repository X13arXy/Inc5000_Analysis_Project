SELECT industry, ROUND(AVG(`growth_%`), 2) as avg_growth
FROM inc_5000_2019
GROUP BY industry
ORDER BY avg_growth DESC
LIMIT 5;