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
    return "hi"

@app.route("/ticker/<symbol>/<domain>")
def ticker(symbol, domain):
    return render_template("ticker.html", symbol=symbol, domain=domain, finnhubKey=FINNHUB_KEY)

# @app.route('/symbol/<symbol>')
# def get_symbol(symbol):

#     finnhub_client = finnhub.Client(api_key=FINNHUB_KEY)
#     symbol_data = finnhub_client.quote(symbol.upper())

#     return render_template("index.html", symbol=symbol, finnhubKey=FINNHUB_KEY)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)