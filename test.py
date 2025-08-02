from flask import Flask, render_template
import weatherd

import weatherImages
import switchWeather

app = Flask(__name__)

@app.route('/')
def index():
    weather = weatherd.getweather()
    return_image = switchWeather.switchweather(weather)
    return render_template('index.html', image=return_image, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
