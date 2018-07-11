import json

from flask import request

from const import *
from const_movimiento import *
from middleware import DATA_PROVIDER
from utilidades.SQL import *


def movimientos():
    cursor = DATA_PROVIDER.conn.cursor()
    cursor.execute(generateSELECT(TABLE, None, True, None))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps(query_result)


def movimiento():
    empleado = request.json["Empleado"]
    cursor = DATA_PROVIDER.conn.cursor()
    cursor.execute(generateSELECT(TABLE, None, True, " {0} {1} = '{2}'".format(WHERE, EMPLEADO, empleado)))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps({'Respuesta': len(query_result) != 0})


def movimientocreate():
    try:
        id = generateUnicId(11)
        empleado = request.json["Empleado"]
        producto = request.json["Producto"]
        cantidad = request.json["Cantidad"]
        valor = request.json["Valor"]
        fechaItem = request.json["Fecha_Item"]
        fechaPago = request.json["Fecha_Pago"]
        valorTotal = request.json["Valor_Total"]
        valorPago = request.json["Valor_Pago"]
        Saldo = request.json["Saldo"]
        filler = ""
        cursor = DATA_PROVIDER.conn.cursor()
        cursor.execute(generateINSERT(TABLE, COLUMS, "({0}, '{1}', {2}, '{3}', '{4}', '{5}', '{6}', '{7}', "
                                                     "'{8}', '{9}')".format(empleado, producto, cantidad,
                                                                                       valor, fechaItem, fechaPago,
                                                                                       valorTotal, valorPago, Saldo,
                                                                                       filler)))
        cursor.commit()
        return json.dumps({'uid': id})
    except Exception as excep:
        return json.dumps({'Respuesta': 'False'})





