from decouple import config
from decimal import Decimal, getcontext
from flask import Blueprint
from flask import Response, json, jsonify
import requests
from flask_cors import cross_origin

blueprints_bp = Blueprint("methods_not_allowed", __name__)

class AutoConfig(object):
    """
    Autodetects the config file and type.
    """
    SUPPORTED = {
        'settings.ini': RepositoryIni,
        '.env': RepositoryEnv,
    }


API = config("QUOTE_API")


@blueprints_bp.route("/", methods=["POST", "DELETE", "PUT", "PATCH"])
@cross_origin()
def methods_not_allowed():
    return "This method is not permited", 403


@blueprints_bp.route("/", methods=["GET"])
@cross_origin()
def current_quote():
    getcontext().prec = 3
    response = requests.get(API)
    dollar_brl_bid = float(abs(Decimal(response.json()["USDBRL"]["bid"])))
    dollar_brl_ask = float(Decimal(response.json()["USDBRL"]["ask"]))
    eu_brl_bid = float(Decimal(response.json()["EURBRL"]["bid"]))
    eu_brl_ask = float(Decimal(response.json()["EURBRL"]["ask"]))
    btc_brl_bid = float(Decimal(response.json()["BTCBRL"]["bid"]))
    btc_brl_ask = float(Decimal(response.json()["BTCBRL"]["ask"]))
    data_quotes = {
        "USDBRL": f"{dollar_brl_bid}",
        "EURBRL": f"{eu_brl_bid}",
        "BTCBRL": f"{btc_brl_bid}",
    }


    return jsonify(data_quotes)
