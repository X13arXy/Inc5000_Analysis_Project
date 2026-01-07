SELECT state, COUNT(*) as count, SUM(revenue) as total_revenue
FROM inc_5000_2019
GROUP BY state
ORDER BY total_revenue DESC
LIMIT 5;