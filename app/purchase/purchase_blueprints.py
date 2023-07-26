from flask import Blueprint, render_template, request, jsonify, redirect
from app.home.home_blueprints import get_crypto_value
from app.models import Movements
from app import db
from datetime import datetime

# Blueprint Configuration
purchase_blueprints = Blueprint(
    "purchase_blueprints", __name__, template_folder="templates", static_folder="static"
)


@purchase_blueprints.route("/purchase", methods=["GET"])
def purchase():
    """Purchase Dashboard."""
    return render_template(
        "purchase.html"
    )


@purchase_blueprints.route("/submit-form", methods=["GET", "POST"])
def submit_form():
    data = request.get_json()
    fro = data['from']
    q1 = data['q1']
    to = data['to']
    q2 = data['q2']
    pu = data['pu']
    print(type(q1))
    print((fro))
    crypto_value_in_euros = get_crypto_value(fro)
    print(type(crypto_value_in_euros))
    print(crypto_value_in_euros)
    amount_in_euros = q1 * crypto_value_in_euros
    print(crypto_value_in_euros, amount_in_euros)
    from datetime import date
    date = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time = current_time
    record = Movements(date=date, time=time, currency_from_text=q1, amount_from_real=fro, moneda_to=to,
                       amount_to=amount_in_euros, pu=float(q1)*float(amount_in_euros))
    db.session.add(record)
    db.session.commit()
    print("Ended")
    return redirect('/')
