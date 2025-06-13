#import
import matplotlib.pyplot as plt
import pandas as pds
import mysql.connector as pymysql

#connector set up
db = pymysql.connect(
    host='localhost',           # 連線主機名稱
    user='root',                # 登入帳號
    password='',
    database = "f1180024"   # 連接指定的 DATABASE
)

#try
cursor = db.cursor()
cursor.execute("SELECT * FROM employee ORDER BY 目前月薪資 ASC;")
results = cursor.fetchall()
for row in results:
    print('row = %r' % (row,))
df = pds.DataFrame(results).to_numpy()

# 關閉連線
cursor.close()
db.close()

#try more
print(df)
ploty = []
for i in range(len(df)):
    ploty.append(df[i, 7])

# 修正：設定中文字體
plt.rcParams["font.sans-serif"] = ["MingLiU"]  # 改用清單格式
plt.rcParams["axes.unicode_minus"] = False
#main
plt.plot(range(len(ploty)), ploty)
plt.title("月薪資分佈", fontsize=18)
plt.xlabel("員工", fontsize=12)
plt.ylabel("月薪資", fontsize=12)
plt.show()
