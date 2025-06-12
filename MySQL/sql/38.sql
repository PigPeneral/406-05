USE madb_n;
SELECT emp.ENAME AS 僱員,
	emp.JOB AS 職務,
    CASE 
		WHEN emp.COMM IS NULL THEN emp.SAL
		ELSE emp.SAL + emp.COMM
	END AS "[薪資+傭金]",
    salgrade.GRADE AS 等級
    FROM emp
INNER JOIN salgrade
    ON CASE
		WHEN emp.COMM IS NULL THEN emp.SAL
		ELSE emp.SAL + emp.COMM 
    END BETWEEN salgrade.LOSAL AND salgrade.HISAL
		AND salgrade.GRADE = 2