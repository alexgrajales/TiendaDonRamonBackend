from flask import Flask
from flask_restful import Api
from clientes.routes import init_api_routes_clientes
from empleados.routes import init_api_routes_empleados

app = Flask(__name__)
api = Api(app)
init_api_routes_clientes(app)
init_api_routes_empleados(app)

if __name__ == '__main__':
     app.run(port='5002')