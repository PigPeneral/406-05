from Connector import alchemy_engine, pd_read, command_select

#未來計畫引進物件導向設計 class 和 除錯，這個idea的雛形做出來後，除錯過程有AI參與，我很高興AI沒有改掉太多，我的邏輯流程應該是對的！

def main():
    while True:
        print("程式用於測試Python程式之間的import，預期的輸出結果為課堂練習的題目答案")
        questionSQ = input("輸入題目題號： ")
        engine = alchemy_engine() #從Connector引進方法，並在這裡建立連線
        command = command_select(questionSQ) #從Connector的字典取得指令內容
        print("使用指令："+f"{command}")
        pd_read(command, engine) #將指令內容傳送給已連線的資料庫，並輸出

if __name__ == '__main__':
    main()