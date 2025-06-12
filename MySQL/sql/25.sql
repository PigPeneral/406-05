USE madb_n;	
SELECT emp1.ENAME AS 姓名, emp2.ENAME AS 主管姓名 FROM emp AS emp1
INNER JOIN emp AS emp2 ON emp1.MGR = emp2.EMPNO