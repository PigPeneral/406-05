#def main
#原本使用了global變數讓變數能在函式之間被使用，AI解釋時建議將區域變數打包起來call到函式即可。AI說我在濫用全域變數。
#網路上的「好的python習慣」希望設計者增加'__main__'和main()以及定義輸入的值的類別。

def main():
    while True:
        option = int(input("選擇排版類型：(1)置左 (2)置中 (3)置右 (0)結束程式　"))
        if option == 0:
            break
        print_dir = int(input("選擇排列方式：(1)向下遞增 (2)向下遞減 (0)返回　"))
        if print_dir == 0:
            continue
        level = int(input("輸入高度:　"))  # 輸入層數
        width = 2 * level - 1  # 計算寬度，高寬數列前幾數為1, 3, 5, 7..... 是等差的
        tri_setup(option, print_dir, width, level)

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
def tri_setup(option, print_dir, width, level):
    for i in range(1, level + 1):
        space = level - i  # AI算法。space是每層(i)開始時，計算每層需要輸出的空格數，因為每一層要輸出的元素和層數相等，所以其餘的空間都是空格的
        if print_dir == 2:
            space = i - 1  # 改變空白數量
        if option == 1:
            tri_left(space, print_dir, width, level)
        elif option == 2:
            tri_mid(space, width)
        elif option == 3:
            tri_right(width, print_dir, i)
        print() #換行

def tri_left(space, print_dir, width, level):
    for row in range(width):
        if print_dir == 1: #向下遞增
            for j in range(level-space):
                print("●", end="")
                if j != level-space:
                    print("　", end="")
            break

        elif print_dir == 2:
            print("●", end="")
            if row == space:  # 向下遞減，這是我意外先寫出來的結果
                break
            print("　", end="")
            continue

def tri_mid(space, width):
    for row in range(width):  # 輸出與寬度相等的內容，j 從 0 開始
        if space <= row < width - space:  #置中。簡化成連鎖比較。AI算法，控制列印元素進行位置的判斷
            posit = row - space  # 計算位置
            if posit == row - space:  # 餘數為0
                print("●", end="")
            else:
               print("　", end="")
        else:
           print("　", end="")


def tri_right(width, print_dir, i): #我反覆使用AI，並來回思考過了幾次，並嘗試不同寫法
    elements_count = i
    for row in range(width):
        if print_dir == 1 :
            posit = width - 1 - row
            if posit < elements_count * 2 - 1:
                if posit % 2 == 0:
                    print("●", end="")
                else:
                    print("　", end="")
            else:
                print("　", end="")

        elif print_dir == 2:
            pass

def tri_fusion():
    pass #待補，菱形等變形

'''
菱形，置左，遞增後遞減
        for j in range(level-space):
            print("●", end="")
            if j < space:
               print("　", end="")
            else:
               break
        break
'''

#main
if __name__ == '__main__':
    main()