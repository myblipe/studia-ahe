from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    city = 'Jelenia Gora'
    if request.method == 'POST':
        city = request.form['city']
    api_key = 'dff7b5776a70ad863421e9f2ff5b9543'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    weather_data = requests.get(url).json()
    return render_template('index.html', weather_data=weather_data, city=city)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
