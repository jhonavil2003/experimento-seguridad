from flask_restful import Resource
from modelos import db

from modelos import UsuarioSchema, Usuario

usuario_schema = UsuarioSchema()

class VistaServicios (Resource) :
    def get(self, id_usuario):
        usuario = db.get_or_404(Usuario, id_usuario)
        if not usuario:
            return {"mensaje": "No existe el usuario"}, 404

        return usuario_schema.dump(usuario)


