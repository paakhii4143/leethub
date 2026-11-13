# Write your MySQL query statement below
SELECT DISTINCT s.*
FROM Stadium s
WHERE s.people >= 100
AND s.id IN (
    SELECT s1.id
    FROM Stadium s1
    JOIN Stadium s2 ON s2.id = s1.id + 1
    JOIN Stadium s3 ON s3.id = s1.id + 2
    WHERE s1.people >= 100
      AND s2.people >= 100
      AND s3.people >= 100
)
OR s.id IN (
    SELECT s2.id
    FROM Stadium s1
    JOIN Stadium s2 ON s2.id = s1.id + 1
    JOIN Stadium s3 ON s3.id = s1.id + 2
    WHERE s1.people >= 100
      AND s2.people >= 100
      AND s3.people >= 100
)
OR s.id IN (
    SELECT s3.id
    FROM Stadium s1
    JOIN Stadium s2 ON s2.id = s1.id + 1
    JOIN Stadium s3 ON s3.id = s1.id + 2
    WHERE s1.people >= 100
      AND s2.people >= 100
      AND s3.people >= 100
)
ORDER BY s.visit_date;