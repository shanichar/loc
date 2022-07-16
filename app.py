import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    area = request.form['Area']
    
    return render_template('results.html', area=area)


if __name__=='__main__':
    app.debug = True
    app.run()

