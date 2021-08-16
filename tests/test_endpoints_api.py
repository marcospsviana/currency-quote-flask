import pytest
from decouple import config
import requests
from datetime import datetime, date
import responses
import sys
from decimal import Decimal, getcontext
from flask import testing
import os
from pathlib import Path


API = "http://exemple.com"

DADOS = {
    "USDBRL": {
        "code": "USD",
        "codein": "BRL",
        "name": "Dólar Americano/Real Brasileiro",
        "high": "5.734",
        "low": "5.7279",
        "varBid": "-0.0054",
        "pctChange": "-0.09",
        "bid": "5.7276",
        "ask": "5.7282",
        "timestamp": "1618315045",
        "create_date": "2021-04-13 08:57:27",
    }
}


@responses.activate
def return_dollar_format():
    responses.add(responses.GET, API, json=DADOS)
    dollar = requests.get(API)
    sys.__stdout__.write(str(Decimal(dollar.json()["USDBRL"]["ask"])))
    money = Decimal(dollar.json()["USDBRL"]["ask"])
    return float(money)


@responses.activate
def test_date_now_returned():
    responses.add(responses.GET, API, json=DADOS)
    response = requests.get(API)
    if response.ok:
        create_date = datetime.fromisoformat(response.json()["USDBRL"]["create_date"])
        assert create_date.date() == date(2021, 4, 13)


@responses.activate
def test_return_dollar():
    responses.add(responses.GET, API, json=DADOS)
    dollar = requests.get(API)
    assert dollar.json()["USDBRL"] != None


def test_return_value_correct_dollar():
    dollar = return_dollar_format()
    assert dollar == 5.7282


@responses.activate
def test_calc_quote_conversion():
    responses.add(responses.GET, API, json=DADOS)
    dollar = requests.get(API)
    getcontext().prec = 8
    dollar = float(Decimal(dollar.json()["USDBRL"]["ask"]))
    sys.__stdout__.write(f"dollar atual {dollar}")
    assert dollar * 2 == 11.4564
