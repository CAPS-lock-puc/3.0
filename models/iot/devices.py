from models.db import db

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # sensor ou atuador

    historicos = db.relationship('Historico', backref='device', lazy=True)
    sensors = db.relationship('Sensor', backref='device', lazy=True)
    actuators = db.relationship('Atuador', backref='device', lazy=True)
    