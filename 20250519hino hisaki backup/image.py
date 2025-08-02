import tkinter #Pythonの使えない機能を解除　tkinter ウィンドウ表示機能
import weatherd
import winsound_1
import weatherImages
import switchWeather
text_id= None
def printweather():
    global text_id
    winsound_1.stop_sound()
    weather = weatherd.getweather()
    print(weather)
    if text_id is not None:
        window.delete(text_id)
    text_id = window.create_text(370, 450, text=weather, font=("Meiryo", 20), fill="#006888")
    return_image = switchWeather.switchweather(weather, images)
    winsound_1.play_sound(weather)
    window.itemconfig(image_id, image=return_image)
hambarg = tkinter.Tk()
hambarg.iconbitmap(default="imagenew/favicon.ico")
#Tk()はtkinterの機能を表す。最初にこいつを呼び出しておく。
hambarg.title("hey!")
hambarg.state("zoomed") #()はウィンドウのタイトル設定
images=weatherImages.weatherimage()
#ウィンドウ作成　#Canvasはウィンドウ本体
window = tkinter.Canvas(hambarg, width=images[0].width(),height=images[0].height()+390)
#image_3の画像の大きさとウィンドウの大きさを比例させる。
#これまで入力したウィンドウのパーツをくっつける
image_id=window.create_image(0, 0, image=images[0], anchor='nw')
#Q.変換した画像の左上をどっから生成しますか？　A.左上　これをミスるとウィンドウに画像が出なくなる
#画面サイズ
button2 = tkinter.Button(window, text="天気を取得",command=printweather)
button2.place(x=340, y=500)
window.pack()
hambarg.mainloop()
#tkinter実行宣言