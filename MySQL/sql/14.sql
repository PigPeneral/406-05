use madb_n;
select ENAME AS 姓名,concat('B',right(ENAME, length(ENAME)-1)) AS 調整後姓名, job AS 職務 from emp where job like 'salesman'