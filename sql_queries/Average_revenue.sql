SELECT industry, ROUND(AVG(revenue), 0) as avg_revenue
FROM inc_5000_2019
GROUP BY industry
ORDER BY avg_revenue DESC
LIMIT 5;