USE madb_n;
SELECT E0.JOB AS 職務,
	E0.ENAME AS 姓名,
	MAX(E0.SAL) AS 最高薪
    FROM emp E0
INNER JOIN 
	(SELECT JOB, MAX(SAL) AS EUP FROM emp GROUP BY JOB) AS E1
	ON E1.JOB = E0.JOB AND E1.EUP = E0.SAL
GROUP BY E0.JOB, E0.ENAME
ORDER BY E0.JOB ASC