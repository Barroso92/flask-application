"""Logged-in page routes."""
import requests
from flask import Blueprint, render_template
from app.models import Movements

COINAPI_KEY = "68C3DF74-1655-42C1-B028-43719BC34A33"

# Blueprint Configuration
home_blueprints = Blueprint(
    "home_blueprints", __name__, template_folder="templates", static_folder="static"
)


# Fetch the current value of a cryptocurrency in euros from CoinAPI
def get_crypto_value(crypto):
    url = f"https://rest.coinapi.io/v1/exchangerate/{crypto}/EUR"
    headers = {'X-CoinAPI-Key': COINAPI_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        crypto_value_in_euros = data['rate']
        return crypto_value_in_euros
    else:
        return None


@home_blueprints.route('/get_crypto_value/<crypto>')
def get_crypto_val(crypto):
    url = f"https://rest.coinapi.io/v1/exchangerate/{crypto}/EUR"
    headers = {'X-CoinAPI-Key': COINAPI_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        crypto_value_in_euros = data['rate']
        return f"The value of {crypto} in euros is: {crypto_value_in_euros}"
    else:
        return "Error fetching data from CoinAPI."


@home_blueprints.route("/", methods=["GET"])
def dashboard():
    Record = Movements.query.all()
    """User Dashboard."""
    return render_template(
        "index.html",
        title="Flask-Login Tutorial",
        template="dashboard-template",
        body="You are now logged in!",
        Record=Record
    )
