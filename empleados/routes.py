from view import *

def init_api_routes_empleados(app):
    if app:
        app.add_url_rule('/api/usuarios/', 'usuarios', usuarios, methods=['GET'])
        app.add_url_rule('/api/createusers/', None, usuarioscreate, methods=['POST'])
        app.add_url_rule('/api/usuario/', 'usuario', usuario, methods=['POST'])
        app.add_url_rule('/api/deleteusers/<string:codigo>', None, usuariosdelete, methods=['DELETE'])
        app.add_url_rule('/api/updateusers/', None, usuariosupdate, methods=['PUT'])
