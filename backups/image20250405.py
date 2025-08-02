import tkinter #Pythonの使えない機能を解除　tkinter ウィンドウ表示機能
import cv2 #画像編集、表示ソフト
from PIL import Image, ImageTk #PILの中から2つを取り出す
import weatherd
import winsound
count=1
rsound=None
def play_rainysound():
    winsound.PlaySound(r"C:\dev\hino hisaki\rain.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
#rsound=multiprocessing.Process(target=play_rainysound)
#()つけると関数の呼び出し   #非同期←実行している間に他のを動かしても可 #定義名の後には：#def=プログラムを動かす準備をする
def stop_rainysound():
    winsound.PlaySound(None, winsound.SND_PURGE)
def change_image():
    global count ,image_id,rsound #グローバル化
    stop_rainysound()
    if count == 0:
        print("sunny")
        window.itemconfig(image_id,image=image_4)
    elif count == 1:
        print("cloudy")
        window.itemconfig(image_id,image=apple)
    elif count == 2:
        print("rainy")
        window.itemconfig(image_id,image=turtle)
        play_rainysound()
    count = (count+1)%3
def printweather():
    weather=weatherd.getweather()
    print(weather)
    window.create_text(370,450,text=weather, font=("Meiryo",20),fill="#32527B")
hambarg = tkinter.Tk()
hambarg.state('zoomed') #フルスクリーンにする
#Tk()はtkinterの機能を表す。最初にこいつを呼び出しておく。
hambarg.title("hey!") #()はウィンドウのタイトル設定

image_1 = cv2.imread(r"imagenew\NKPF2927.PNG")
#imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
image_2= cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)
#cv2の機能、cvtColorがimage_1を変換する
image_3 = Image.fromarray(image_2)
#fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
image_4 = ImageTk.PhotoImage(image_3)

white = cv2.imread(r"imagenew\KHKPE8767.PNG")
#imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
hey= cv2.cvtColor(white, cv2.COLOR_BGR2RGB)
#cv2の機能、cvtColorがimage_1を変換する
sup = Image.fromarray(hey)
#fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
apple = ImageTk.PhotoImage(sup)
#tkinterで表示するための画像フォーマット変換

moniter = cv2.imread(r"imagenew\UEMN8804.PNG")
#imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
happy= cv2.cvtColor(moniter, cv2.COLOR_BGR2RGB)
#cv2の機能、cvtColorがimage_1を変換する
qwerty = Image.fromarray(happy)
#fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
turtle = ImageTk.PhotoImage(qwerty)
#tkinterで表示するための画像フォーマット変換

#ウィンドウ作成　#Canvasはウィンドウ本体
window = tkinter.Canvas(hambarg, width=image_3.width, height=image_3.height+390)
#image_3の画像の大きさとウィンドウの大きさを比例させる。
#これまで入力したウィンドウのパーツをくっつける
image_id=window.create_image(0, 0, image=image_4, anchor='nw')
#Q.変換した画像の左上をどっから生成しますか？　A.左上　これをミスるとウィンドウに画像が出なくなる
#画面サイズ
button1 = tkinter.Button(window, text="天気を変更",command=change_image)
# placeによる配置
button1.place(x=200, y=500)
button2 = tkinter.Button(window, text="天気を取得",command=printweather)
button2.place(x=500, y=500)

window.pack()
hambarg.mainloop()
#tkinter実行宣言
