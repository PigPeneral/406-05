USE madb_n;
SELECT emp1.ENAME AS 姓名, emp1.HIREDATE AS 到職日, emp2.ENAME AS 主管, emp2.HIREDATE AS 到職日 FROM emp as emp1
INNER JOIN emp as emp2 ON emp1.MGR = emp2.EMPNO
WHERE emp1.HIREDATE < emp2.HIREDATE