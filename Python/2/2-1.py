#def main
#原本使用了global變數讓變數能在函式之間被使用，AI解釋時建議將區域變數打包起來call到函式即可。AI說我在濫用全域變數。
#網路上的「好的python習慣」希望設計者增加'__main__'和main()以及定義輸入的值的類別。
def main():
    while True:
        op = int(input("選擇排版類型：(1)置左 (2)置中 (3)置右 (0)結束程式　"))
        if op == 0:
            break
        c = int(input("選擇排列方式：(1)向下遞增 (2)向下遞減 (0)返回　"))
        if c == 0:
            continue
        lev = int(input("輸入高度:　"))  # 輸入層數
        width = 2 * lev - 1  # 計算寬度，高寬數列前幾數為1, 3, 5, 7..... 是等差的
        tri_setup(op, c, width, lev)

'''
我感覺自己在調整迴圈上思考太久，老師的示範中變數較多，我理解起來比較緩慢，此程式最終使用Claude AI進行輔助。
讓Claude提供數字規律轉換為迴圈的寫法，並且要求他從預想的輸出結果中找到規律，我再透過閱讀理解，接著擴寫成我的版本。
*第一次指令中僅用文字指示，沒有提供預期的輸出內容，AI產生的代碼使用"spaces = (max_elements - row) // 2"計算所需空格。
其中max_elements = height(金字塔層數) 為底層元素數量。
程式在每次迴圈計算一次空格數，並以相同次數輸出空格，元素即row(range(1, height+1))這與我原本想的迴圈一樣。
**第二次指令提供了輸出內容，他也確實理解了規律，在產生的程式中，他的回答和程式註解表示應採用奇數偶數的規律調整出輸出的位置。
<!--我會在程式盡量鍵入我的理解過程和解讀，註解可能會導致程式的文字量有點多。-->
'''
#def misc.
def valid_inputs(n): #輸入檢測(待完成)
    try:
        n = str(n)
        if  len(n.strip()) == 0:
            return False
        n = int(n)
    except ValueError:
        print("無效數值，請重新輸入！")
        return False
    else:
        return True

#tri main
#AI使用了函式print_row去接受各tri函式的結果，並輸出。但是它十分精簡，我在理解上需要做比較多展開並思考的動作，所以我在這邊不打算採用。
#但是我仍然會努力增加程式容易閱讀的部分
def tri_setup(op, c, width, lev):
    for i in range(1, lev + 1):
        ss = lev - i  # AI算法。ss是每層(i)開始時，計算每層需要輸出的空格數，因為每一層要輸出的元素和層數相等，所以其餘的空間都是空格的
        if op == 1:
            tri_left(ss, op, c)
        for j in range(width):  # 輸出與寬度相等的內容，j 從 0 開始
            if op == 2:
                tri_mid(j, ss, op, c)
            elif op == 3:
                tri_right(j, ss, op, c)
        print() #換行

def tri_left(ss, c, width):
    for i in range(width):
        print("●", end="")
        if i == ss and c == 2:  # 向下遞減，這是我意外先寫出來的結果
            break
        print("　", end="")
        continue

def tri_mid(j, ss, c, width):
    if ss <= j < width - ss and c == 1:  # 向下遞增，置中。簡化成連鎖比較。AI算法，控制列印元素進行奇偶數位置的判斷
        p = j - ss  # 計算位置
        if p % 2 == 0:  # 餘數為0，表示偶數(可處理負數)
            print("●", end="")  # 元素都在偶數格
        else:
            print("　", end="")  # 空格都在奇數格
    else:
        print("　", end="")

def tri_right(j, ss, c, lev):
    if c == 1: # 向下遞增
        if j != ss:  # 先將空格輸出完
            print("　", end="")
        else:
            for i in range(lev - ss):  # 反推該層元素數
                print("●", end="")
    if c == 2: # 向下遞減 *輸出問題
        if j <= (lev-ss): # 先將空格輸出完
            print("　", end="")
        else:
            for i in range(abs(ss-lev)):  # 反推該層元素數
                print("●", end="")

def tri_fusion():
    pass #待補，菱形等變形
#main
if __name__ == '__main__':
    main()