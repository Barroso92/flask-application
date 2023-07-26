from flask import Blueprint, render_template
from sqlalchemy import func
import sqlite3
from app.home.home_blueprints import get_crypto_value
from app import db
from app.models import Movements

# Blueprint Configuration
status_blueprints = Blueprint(
    "status_blueprints", __name__, template_folder="templates", static_folder="static"
)


@status_blueprints.route("/status", methods=["GET"])
def status():
    distinct_values = db.session.query(Movements.amount_from_real.distinct()).all()
    distinct_values = [value[0] for value in distinct_values]

    sum_of_distinct_values = db.session.query(func.sum(Movements.currency_from_text)).scalar()

    sum_of_distinct_values_two = db.session.query(func.sum(Movements.amount_to)).scalar()

    Inversion = sum_of_distinct_values + sum_of_distinct_values_two

    return render_template('status.html', distinct_values=distinct_values,
                           sum_of_distinct_values=sum_of_distinct_values,
                           sum_of_distinct_values_two=sum_of_distinct_values_two,
                           Inversion=Inversion)
