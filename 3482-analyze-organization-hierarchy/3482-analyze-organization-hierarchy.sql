# Write your MySQL query statement below
WITH RECURSIVE hierarchy AS (
    -- CEO starts at level 1
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Each employee is one level below their manager
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        h.level + 1
    FROM Employees e
    JOIN hierarchy h
        ON e.manager_id = h.employee_id
),

reporting AS (
    -- Every employee is initially their own report
    SELECT
        employee_id AS manager_id,
        employee_id AS report_id
    FROM Employees

    UNION ALL

    -- Find all direct and indirect reports
    SELECT
        r.manager_id,
        e.employee_id
    FROM reporting r
    JOIN Employees e
        ON e.manager_id = r.report_id
),

team AS (
    SELECT
        r.manager_id,
        COUNT(*) - 1 AS team_size,
        SUM(e.salary) AS budget
    FROM reporting r
    JOIN Employees e
        ON r.report_id = e.employee_id
    GROUP BY r.manager_id
)

SELECT
    h.employee_id,
    h.employee_name,
    h.level,
    t.team_size,
    t.budget
FROM hierarchy h
JOIN team t
    ON h.employee_id = t.manager_id
ORDER BY
    h.level ASC,
    t.budget DESC,
    h.employee_name ASC;