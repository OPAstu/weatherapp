from flask import Flask, render_template

app = Flask(__name__)

# 天気ごとの画像辞書
weather_images = {
    "晴れ": "static/imagenew/sunny.png",
    "くもり": "static/imagenew/cloudy.png",
    "雨": "static/imagenew/rainy.png",
    "雪": "static/imagenew/snowy.png",
    "雷": "static/imagenew/thunder.png"
}

@app.route('/')
def index():
    # ここで天気情報を手動で変更
    current_weather = "晴れ"  # 例として「晴れ」を設定

    # 天気情報に基づいて画像パスを取得
    image_path = weather_images.get(current_weather, weather_images["晴れ"])

    return render_template('index.html', image_path=image_path, current_weather=current_weather)

if __name__ == '__main__':
    app.run(debug=True)
