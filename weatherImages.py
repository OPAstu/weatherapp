import cv2
from PIL import Image

def images2(weather):
    # 天気に応じた画像を辞書として管理
    images = {
        "晴れ": Image.fromarray(cv2.cvtColor(cv2.imread("static/imagenew/sunny.PNG"), cv2.COLOR_BGR2RGB)),
        "曇り": Image.fromarray(cv2.cvtColor(cv2.imread("static/imagenew/cloudy.PNG"), cv2.COLOR_BGR2RGB)),
        "雨": Image.fromarray(cv2.cvtColor(cv2.imread("static/imagenew/rainy.PNG"), cv2.COLOR_BGR2RGB)),
        "雪": Image.fromarray(cv2.cvtColor(cv2.imread("static/imagenew/snowy.PNG"), cv2.COLOR_BGR2RGB)),
        "雷": Image.fromarray(cv2.cvtColor(cv2.imread("static/imagenew/thunder.PNG"), cv2.COLOR_BGR2RGB)),
    }
    
    # 天気情報に基づいて画像を選択
    return images.get(weather, images["晴れ"])  # 天気が辞書にない場合は "晴れ" を返す
