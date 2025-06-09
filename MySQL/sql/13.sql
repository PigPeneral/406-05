use madb_n;
select ENAME AS 姓名, concat(left(ENAME, 3), rpad('', length(ENAME)-3,'*')) AS 前三字元 from emp 