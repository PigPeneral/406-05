#9x9
#試著盡量自己寫了，在不改變使用指令的模式和狀況下，對齊的部分，還在思考要如何從根本解決
list1 = []
list2 = []
list3 = []
for i in range(1, 10): #讓i從1跑到9，range數不到指定數(我理解為：他一看到指定數字便會停止，便不繼續框列數字，因此會沒有最後一個數)
    for j in range(1, 10): #同理，但是i會先跑
        list1.append("%d*%d=%2d" % (i, j, i*j)) #百分比(%) *據說是比較C語言的寫法，或許我記錯了
        list2.append("{:d}*{:d}={:2d}".format(i, j ,i*j)) #str.format 給定字串空間{:}，貼上標籤{d}，然後使用.format逐一給值
        list3.append(f"{i}*{j}={i*j:2}") #f-string *{變數:2}讓他預留2格
    list1.append("\n")
    list2.append("\n")
    list3.append("\n")

list_tag=["1.百分比", "2.str.format", "3.f-string"]
print(list_tag[0])
for i in range(len(list1)):
    print(list1[i], end=" ")
print(list_tag[1])
for i in range(len(list2)):
    print(list2[i], end=" ")
print(list_tag[2])
for i in range(len(list3)):
    print(list3[i], end=" ")