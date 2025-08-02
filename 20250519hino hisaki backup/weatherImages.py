import cv2 #画像編集、表示ソフト
from PIL import Image, ImageTk 
def weatherimage():
    global weatherimage
    image_1 = cv2.imread(r"imagenew/sunny.PNG")
    #imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
    image_2= cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)
    #cv2の機能、cvtColorがimage_1を変換する
    image_3 = Image.fromarray(image_2)
    #fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
    image_4 = ImageTk.PhotoImage(image_3)

    white = cv2.imread(r"imagenew/cloudy.PNG")
    #imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
    hey= cv2.cvtColor(white, cv2.COLOR_BGR2RGB)
    #cv2の機能、cvtColorがimage_1を変換する
    sup = Image.fromarray(hey)
    #fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
    apple = ImageTk.PhotoImage(sup)
    #tkinterで表示するための画像フォーマット変換

    moniter = cv2.imread(r"imagenew/rainy.PNG")
    #imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
    happy= cv2.cvtColor(moniter, cv2.COLOR_BGR2RGB)
    #cv2の機能、cvtColorがimage_1を変換する
    qwerty = Image.fromarray(happy)
    #fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
    turtle = ImageTk.PhotoImage(qwerty)
    #tkinterで表示するための画像フォーマット変換
    
    snow= cv2.imread(r"imagenew/snowy.PNG")
    #imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
    ym= cv2.cvtColor(snow, cv2.COLOR_BGR2RGB)
    #cv2の機能、cvtColorがimage_1を変換する
    mine = Image.fromarray(ym)
    #fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
    fufu = ImageTk.PhotoImage(mine)
    #tkinterで表示するための画像フォーマット変換

    ivory = cv2.imread(r"imagenew/thunder.PNG")
    #imreadはcv2の画像読み込み機能。()にはファイルの位置と名前を書く
    pie= cv2.cvtColor(ivory, cv2.COLOR_BGR2RGB)
    #cv2の機能、cvtColorがimage_1を変換する
    qaz = Image.fromarray(pie)
    #fromarrayはimageを受け入れるメモリがあるか確認する機能。PILフォーマットへの変換も兼ねている。
    wsx = ImageTk.PhotoImage(qaz)
    #tkinterで表示するための画像フォーマット変換

    return[image_4,apple,turtle,fufu,wsx]