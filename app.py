import os
from flask import Flask, render_template, jsonify, make_response, request
from dotenv import dotenv_values, load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import requests
import finnhub

app = Flask(__name__)

envVars = dotenv_values(".env")
FINNHUB_KEY = envVars["FINNHUB_KEY"]
TWILIO_ACCOUNT_SID = envVars["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = envVars["TWILIO_AUTH_TOKEN"]
TWILIO_NUMBER = envVars["TWILIO_NUMBER"]
TWILIO_MSG_SID = envVars["TWILIO_MSG_SID"]

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
finnhub_client = finnhub.Client(api_key=FINNHUB_KEY)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/loop/<symbols>")
def loop(symbols):
    return render_template("loop.html", symbols=symbols, finnhubKey=FINNHUB_KEY)

@app.route("/ticker/<symbol>/<domain>")
def ticker(symbol, domain):
    return render_template("ticker.html", symbol=symbol, domain=domain, finnhubKey=FINNHUB_KEY)


@app.route("/price", methods=['GET', 'POST'])
def price():

    quote = finnhub_client.quote(
        (request.values.get('Body', None).upper().strip())
    )
    # print(quote["c"])

    response = MessagingResponse()

    respMessage = request.values.get('Body', None).upper() + ": $"
    respMessage = str(respMessage) + (str(quote["c"]))
    response.message(respMessage)

    # print(response)

    return str(response)


if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(host="0.0.0.0",port=5000,debug=False)
