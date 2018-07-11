from view import *

def init_api_routes_movimientos(app):
    if app:
        app.add_url_rule('/api/movimientos/', 'movimientos', movimientos, methods=['GET'])
        app.add_url_rule('/api/createmovimiento/', None, movimientocreate, methods=['POST'])
        app.add_url_rule('/api/movimiento/', 'movimiento', movimiento, methods=['POST'])

