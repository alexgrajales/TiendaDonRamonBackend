from view import clientes
from view import cliente
from view import revisarcleardb

def init_api_routes_clientes(app):
    if app:
        app.add_url_rule('/api/clientes', 'clientes', clientes, methods=['GET'])
        app.add_url_rule('/api/clientes/<string:codigo>', 'cliente', cliente, methods=['GET'])
        app.add_url_rule('/api/cleardb/', 'cleardb', revisarcleardb, methods=['GET'])
