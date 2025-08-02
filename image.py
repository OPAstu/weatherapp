from flask import Flask, render_template
import requests
import weatherImages
import winsound_1  # 画像選択関数をインポート

app = Flask(__name__)

@app.route('/')
def index():
    # 気象庁の天気予報データを取得
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    response = requests.get(url)
    weather_data = response.json()
    
    # 東京地方の天気情報を取得
    area_weather = weather_data[0]['timeSeries'][0]['areas'][0]
    # 天気情報に基づいて画像を選択
    image_path = weatherImages.images2(area_weather['weathers'][0])  # 引数として天気を渡す
    
    # Flask テンプレートに画像パスを渡して表示
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
