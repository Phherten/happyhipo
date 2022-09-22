import bs4
import requests
from bs4 import BeautifulSoup


def hipoteca(total, tipo_ofrecido, años):
    total = total
    euribor = euribor_scraping()
    tipo = tipo_ofrecido + euribor
    interes_mensual = (tipo / 12) / 100
    años = años
    cuotas = años * 12
    cuota_mensual = total * (
            (((1 + interes_mensual) ** cuotas) * interes_mensual) / (((1 + interes_mensual) ** cuotas) - 1))

    return round(cuota_mensual)


def euribor_scraping():
    resultado = requests.get('https://www.expansion.com/mercados/euribor.html')
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    valor = sopa.select('tbody tr td')[0]
    euribor = valor.getText()
    decimal = euribor.replace(',', '.')
    return float(decimal)


print(hipoteca(215000,1,25))
