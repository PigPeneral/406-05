#數值判斷
#function
def match_case(n):
    match n: #程式表示這段程式是Unreachable, 我還不確定是為什麼
        case n if n >= 9:
            return "A級"
        case n if 8 <= n < 9: #使用chained comparison，看python官方教學說，C語言好像不能這樣，這是python獨有的連續比較。(PyCharm的弱警告希望我把and簡化成這樣)
            return "B級"
        case n if 7 <= n < 8:
            return "C級"
        case n if 6 <= n < 7:
            return "D級"
        case _:
            return "F級"

#main
while True: #loop it
    score = input("輸入分數 <輸入0以離開> :")

    if len(score.strip()) == 0:  # 空白檢測 .strip method from stack overflow
        print(TypeError)
        continue

    try: #浮數處理
        score = float(score)
    except: #弱警告(未解決)：例外條件過於寬鬆，缺乏針對性
        float_test = False
        pass
    else:
        round(score, 0)
        float_test = True

    try:  # try int **空白檢測要先做，因為字串做不等式會發生錯誤
        score = int(score)
    except ValueError:
        print("請輸入數字！")
        continue

    if score < 0 or score > 100: #range
        print("我不能對小於0或是大於100的數進行操作！")
        continue
    elif score == 0:
        input("任意輸入內容以結束程式")
        break

    if float_test: #PyCharm說：不用讓他檢查test內是否為真，直接讓它決定條件式是否為真即可。
        print("小數部分已取整。")
        print()

    score = int(score)

    print("1.")
    # if else
    if score >= 90:
        print("A級")
    elif 80 <= score < 90:
        print("B級")
    elif 70 <= score < 80:
        print("C級")
    elif 60 <= score < 70:
        print("D級")
    else:
        print("F級")

    # next
    print()
    print("2.")
    # Ternery
    s = ("A級" if score >= 90 else "B級"
    if 80 <= score < 90 else "C級"
    if 70 <= score < 80 else "D級"
    if 60 <= score < 70 else "F級")

    print(s)

    # next
    print()
    print("3.")
    # case match
    s = score / 10
    print(match_case(s))
    print() #視覺調整