import os
from flask import Flask, render_template, jsonify
from dotenv import dotenv_values, load_dotenv
import requests
import finnhub

app = Flask(__name__)

load_dotenv()
FINNHUB_KEY = os.environ.get('FINNHUB_KEY')

@app.route("/")
def index():
    return renter_template("index.html")

@app.route("/ticker/<symbol>/<domain>")
def ticker(symbol, domain):
    return render_template("ticker.html", symbol=symbol, domain=domain, finnhubKey=FINNHUB_KEY)

if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=5000,debug=True)
    app.run(host="0.0.0.0",port=5000,debug=False)