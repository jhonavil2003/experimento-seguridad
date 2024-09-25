from flask_restful import Resource
from flask import request
from modelos import db

from modelos import UsuarioSchema, Usuario

usuario_schema = UsuarioSchema()

class VistaServicios (Resource) :
    def post(self):
        id_usuario = request.json.get("usuario", "")
        usuario = db.get_or_404(Usuario, id_usuario)
        if not usuario:
            return {"mensaje": "No existe el usuario"}, 404

        return usuario_schema.dump(usuario)

class VistaUsuarios (Resource) :
    def post(self):
        usuario = request.json.get("usuario", "")

        if not usuario:
            return {"mensaje": "El campo 'usuario' es obligatorio y no puede estar vacio"}, 400

        usuario_bd = Usuario.query.filter_by(usuario=usuario).first()

        if usuario_bd:
            return {"mensaje": "Usuario ya existe"}, 400

        nuevo_usuario = Usuario(usuario=usuario)

        db.session.add(nuevo_usuario)
        db.session.commit()

        return usuario_schema.dump(nuevo_usuario)
