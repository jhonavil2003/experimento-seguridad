import enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import date
from decimal import Decimal

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(128), unique=True, nullable=False)
    servicios = db.relationship('Servicio', cascade='all, delete, delete-orphan')


class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    descripcion = db.Column(db.String(128), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)

class ServicioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Servicio
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

    servicios = fields.List(fields.Nested(ServicioSchema()))

