SELECT name, industry, `growth_%`, workers, previous_workers
FROM inc_5000_2019
WHERE workers < previous_workers AND `growth_%` > 0
ORDER BY `growth_%` DESC
LIMIT 10;