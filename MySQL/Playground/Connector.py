from sqlalchemy import create_engine
import pandas as pd

#commands to .get 字典方法 我竟然要一個一個寫 我要趕快找到新方法
commands = {
    "1": "SELECT * FROM emp WHERE SAL<40000;",
    "2": "SELECT * FROM emp WHERE DEPTNO=30;",
    "3": "SELECT ENAME AS 姓名, EMPNO AS 員工編號, DEPTNO AS 部門名稱 FROM emp WHERE JOB NOT LIKE 'MANAGER' AND JOB NOT LIKE 'PRESIDENT';",
    "4": "SELECT * FROM emp WHERE SAL<COMM;",
    "5": "SELECT * FROM emp WHERE SAL*0.6 < COMM;",
    "6": "SELECT * FROM emp WHERE JOB LIKE 'MANAGER' AND DEPTNO LIKE 10;",
    "7": "SELECT * FROM emp WHERE JOB NOT LIKE 'MANAGER' AND SAL > 80000;",
    "8": "SELECT ENAME AS 姓名, JOB AS 職務, COMM AS 傭金 FROM emp WHERE COMM NOT LIKE 0;",
    "9": "SELECT * FROM emp WHERE COMM = 0 OR COMM < 12000;",
    "10": "SELECT * FROM emp WHERE HIREDATE < '2012-06-09';",
    "11": "SELECT * FROM emp WHERE HIREDATE < '2012-01-01';",
    "12": "SELECT * FROM emp WHERE ENAME LIKE '_____';",
    "13": """SELECT EMPNO AS 員工編號, ENAME AS "名字不帶'A'" from emp where ENAME not like '%A%';""",
    "14": "SELECT ENAME AS 姓名, RPAD(LEFT(ENAME, 3), LENGTH(ENAME),'*') AS 前三字元 FROM emp;",
    "15": "SELECT ENAME AS 姓名,CONCAT('B',RIGHT(ENAME, LENGTH(ENAME)-1)) AS 調整後姓名, JOB AS 職務 FROM emp WHERE JOB LIKE 'SALESMAN';",
    "16": "SELECT * FROM emp ORDER BY ENAME ASC;",
    "17": "SELECT ENAME AS 姓名, HIREDATE AS 到職日 FROM emp ORDER BY HIREDATE ASC;",
    "18": "SELECT ENAME AS 姓名, JOB AS 職務, SAL AS 薪資 FROM emp ORDER BY JOB ASC, SAL DESC;",
    "19": "SELECT ENAME AS 姓名, SAL AS 薪資, ROUND(SAL/30, 1) AS 日薪 FROM emp;",
    "20": "SELECT ENAME AS 姓名, SAL AS 薪資 FROM emp ORDER BY SAL ASC LIMIT 1;",
    "21": "SELECT ENAME AS 姓名, HIREDATE AS 到職日 FROM emp WHERE HIREDATE LIKE '%-02-%';",
    "22": "SELECT ENAME AS 姓名, HIREDATE AS 到職日, DATEDIFF(CURRENT_TIMESTAMP, HIREDATE) AS 到職天數 FROM emp ORDER BY 到職天數 DESC;",
    "23": "SELECT EMPNO AS 員工編號, ENAME AS 姓名有C僱員 FROM emp WHERE ENAME LIKE '%c%';",
    "24": "SELECT D.DeptNO , DNAME  , E. FROM Dept D INNER JOIN (SELECT DEPTNO, COUNT(*) 人數 FROM emp GROUP BY DEPTNO) E ON D.DEPTNO=E.DEPTNO;",
    "25": "SELECT DEPTNO AS 部門編號, ENAME AS 姓名, SAL AS 薪資 FROM emp WHERE SAL > (SELECT SAL FROM emp WHERE ENAME='SMITH') order by DEPTNO ASC;",
    "26": "SELECT emp1.ENAME AS 姓名, emp2.ENAME AS 主管姓名 FROM emp AS emp1 INNER JOIN emp AS emp2 ON emp1.MGR = emp2.EMPNO;",
    "27": "SELECT emp1.ENAME AS 姓名, emp1.HIREDATE AS 到職日, emp2.ENAME AS 主管, emp2.HIREDATE AS 到職日 FROM emp as emp1 INNER JOIN emp as emp2 ON emp1.MGR = emp2.EMPNO WHERE emp1.HIREDATE < emp2.HIREDATE;",
    "28": "SELECT DISTINCT CLK.ENAME AS 姓名, CLK.JOB AS 職位, dept.DNAME AS 部門名稱 FROM emp, dept INNER JOIN emp AS CLK ON CLK.JOB LIKE 'CLERK' WHERE dept.DEPTNO = CLK.DEPTNO;",
    "29": "SELECT DISTINCT e.JOB AS 職務, e.ENAME AS 僱員, MIN(e.SAL) AS 最低薪 FROM emp AS e INNER JOIN (SELECT JOB, MIN(SAL) AS MIN_LOW FROM emp GROUP BY JOB) AS LOW ON e.JOB = LOW.JOB AND e.SAL = LOW.MIN_LOW GROUP BY e.JOB, e.ENAME ORDER BY e.SAL ASC;",
    "30": "SELECT emp.ENAME AS 僱員, emp.JOB AS 職務 FROM emp INNER JOIN (SELECT ENAME, JOB FROM emp WHERE ENAME LIKE 'SCOTT') AS N ON N.ENAME NOT LIKE emp.ENAME AND N.JOB LIKE emp.JOB;",
    "31": "SELECT DISTINCT E.ENAME AS 僱員, E.SAL AS 薪資 FROM emp AS E INNER JOIN (SELECT ENAME, SAL FROM emp WHERE DEPTNO = 30) AS E30 ON E.SAL = E30.SAL;",
    "32": "SELECT dept.DEPTNO AS 部門編號, dept.DNAME AS 部門名稱, dept.LOC AS 區域, (SELECT COUNT(*) FROM emp WHERE emp.DEPTNO = dept.DEPTNO) AS 人數 FROM dept;",
    "33": "SELECT ENAME AS 僱員, (SELECT DNAME FROM dept WHERE DEPTNO = emp.DEPTNO) AS 部門名稱, SAL AS 薪資 FROM emp;",
    "34": "SELECT DEPTNO AS 部門編號, DNAME AS 部門名稱, LOC AS 區域, (SELECT count(*) FROM emp WHERE DEPTNO=dept.DEPTNO) AS 人數 FROM dept;",
    "35": "SELECT E0.JOB AS 職務, E0.ENAME AS 姓名, MAX(E0.SAL) AS 最高薪 FROM emp E0 INNER JOIN (SELECT JOB, MAX(SAL) AS EUP FROM emp GROUP BY JOB) AS E1 ON E1.JOB = E0.JOB AND E1.EUP = E0.SAL GROUP BY E0.JOB, E0.ENAME ORDER BY E0.JOB ASC;",
    "36": "SELECT E0.ENAME AS 經理, E0.JOB AS 職務, E0.SAL AS 最低薪 FROM emp E0 INNER JOIN (SELECT ENAME, JOB, MIN(SAL) AS LOWS FROM emp WHERE JOB LIKE 'MANAGER') AS E1 ON E1.LOWS = E0.SAL;",
    "37": "SELECT ENAME AS 僱員, JOB AS 職務, SAL*12 AS 年薪 FROM emp ORDER BY SAL DESC;",
    "38": "SELECT emp.ENAME AS 僱員, emp.JOB AS 職務, emp.SAL AS 薪資, salgrade.GRADE AS 等級 FROM emp INNER JOIN salgrade ON emp.SAL BETWEEN salgrade.LOSAL AND salgrade.HISAL AND salgrade.GRADE = 4;",
    "39": """SELECT emp.ENAME AS 僱員, emp.JOB AS 職務, CASE WHEN emp.COMM IS NULL THEN emp.SAL ELSE emp.SAL + emp.COMM END AS "[薪資+傭金]", salgrade.GRADE AS 等級 FROM emp INNER JOIN salgrade ON CASE WHEN emp.COMM IS NULL THEN emp.SAL ELSE emp.SAL + emp.COMM END BETWEEN salgrade.LOSAL AND salgrade.HISAL AND salgrade.GRADE = 2;""",
    "40": "SELECT E0.DEPTNO AS 部門編號, E0.ENAME AS 僱員, E0.JOB AS 職務, E0.SAL AS 薪資 FROM emp E0 WHERE (SELECT COUNT(DISTINCT E1.SAL) FROM emp E1 WHERE E1.DEPTNO = E0.DEPTNO AND E1.SAL > E0.SAL) = 1;"
}

#連線
def alchemy_engine():
    return create_engine('mysql+mysqlconnector://root:@localhost/madb_n')

#選指令
def command_select(questionSQ):
    return commands.get(questionSQ, "SELECT NULL") #預設查詢，若字典取不出值，則預設為"SELECT NULL"

#pd read
def pd_read(command, engine):
    df = pd.read_sql(command, engine)
    print(df)

#sqlalchemy search
#with engine.connect() as connect:
#    result = connect.execute(text(f"{command}"))
#    for row in result:
#        print(row)