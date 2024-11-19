from models.db import db
from datetime import datetime
from models.iot.devices import Device

class Historico(db.Model):
    __tablename__ = 'historico'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    leitura = db.Column(db.String(200), nullable=False)

    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)