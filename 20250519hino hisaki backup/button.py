import tkinter

import tkinter

# メインウィンドウを作成
root = tkinter.Tk()

#画面サイズ
root.geometry("200x150")

# ボタンを作成
button1 = tkinter.Button(root, text="ボタン１")
button2 = tkinter.Button(root, text="ボタン２")
button3 = tkinter.Button(root, text="ボタン３")

# placeによる配置
button1.place(x=10, y=10)
button2.place(x=50, y=50, width=80, height=40)
button3.place(x=200, y=150)

# メインループを開始
root.mainloop()