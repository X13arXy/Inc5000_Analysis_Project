SELECT industry, COUNT(*) as company_count
FROM inc_5000_2019
GROUP BY industry
ORDER BY company_count DESC;