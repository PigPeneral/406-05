USE madb_n;
SELECT ENAME AS 僱員,
	JOB AS 職務,
	SAL*12 AS 年薪
 FROM emp
 ORDER BY SAL DESC