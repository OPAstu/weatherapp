import requests
def getweather():#気象庁データの取得
    weather_url="https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    weather_json=requests.get(weather_url).json()
    #取得したいデータの選択
    weather_cloud = weather_json [0]["timeSeries"][0]["areas"][0] ["weathers"][0] #←上に同じく
    #全角スペースの削除
    weather_cloud=weather_cloud.replace('　','') 
    return(weather_cloud)