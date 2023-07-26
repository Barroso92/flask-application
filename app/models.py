"""Database models."""
from app import db


class Movements(db.Model):
    """User account model."""

    __tablename__ = "movements"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200), index=False, nullable=True)
    time = db.Column(db.String(200), index=False,  nullable=True)
    currency_from_text = db.Column(db.String(100),  nullable=False)
    amount_from_real = db.Column(db.String(100),  nullable=False)
    moneda_to = db.Column(db.String(100),  nullable=False)
    amount_to = db.Column(db.String(100),  nullable=False)
    pu = db.Column(db.String(100),  nullable=False)

    def __int__(self, date, time, currency_from_text, amount_from_real, moneda_to, amount_to, pu):
        self.date = date
        self.time = time
        self.currency_from_text = currency_from_text
        self.amount_from_real = amount_from_real
        self.moneda_to = moneda_to
        self.amount_to = amount_to
        self.pu = pu

