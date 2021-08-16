from flask import Flask, make_response
from flask import Blueprint
from quotes.quotes_api import blueprints_bp


app = Flask(__name__)
app.register_blueprint(blueprints_bp)


if __name__ == "__main__":
    app.run(host="localhost", port=5050, debug=True)
