USE madb_n;
SELECT emp.ENAME AS 僱員,
	emp.JOB AS 職務,
    emp.SAL AS 薪資,
    salgrade.GRADE AS 等級
    FROM emp
INNER JOIN salgrade
    ON emp.SAL BETWEEN salgrade.LOSAL AND salgrade.HISAL 
		AND salgrade.GRADE = 4
-- AI推薦簡單法
-- SELECT emp.ENAME AS 僱員,
--        emp.JOB AS 職務,
--        emp.SAL AS 薪資,
--        salgrade.GRADE AS 等級
-- FROM emp, salgrade
-- WHERE emp.SAL BETWEEN salgrade.LOSAL AND salgrade.HISAL
--   AND salgrade.GRADE = 4;