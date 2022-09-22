from flask import Flask, request
from main import hipoteca
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "LA PAGINA FUNCIONA"


@app.route('/inicio', methods=['POST'])
def inicio():
    request_body = request.get_json()
    bot_token = "5435944228:AAH9T6qKkSAO-zZjEIYkMn1WuHUSQtuxOcM"
    bot_chat_id = str(request_body['bot_chadid'])
    cuota = hipoteca(request_body['total'], request_body['interes_ofrecido'], request_body['años'])
    msg = f'Es Lunes, pero alegrate porque pagarias {cuota} euros de hipoteca si la hubieras cogido variable'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text)
    return "mensaje enviado"
