from middleware import DATA_PROVIDER
from const_empleados import *
from const import *
import json
import MySQLdb
from flask import request
from utilidades.SQL import *
import utilidades.Const

def usuarios():
    cursor = DATA_PROVIDER.conn.cursor()
    cursor.execute(generateSELECT(TABLE, None, True, None))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps(query_result)


def usuario():
    name = request.json["name"]
    password = request.json["password"]
    cursor = DATA_PROVIDER.conn.cursor()
    cursor.execute(generateSELECT(TABLE, None, True, " {0} {1} = '{2}' and {3} = '{4}'".format(WHERE, NOMBRE, name, CLAVE, password)))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps(query_result)


def usuarioscreate():
    try:
        id = generateUnicId(11)
        first_name = request.json["email"]
        ccosto = "0111"#request.form["ccosto"]
        clave = request.json["password"]
        cursor = DATA_PROVIDER.conn.cursor()
        cursor.execute(generateINSERT(TABLE, COLUMS, "({0}, '{1}', {2}, '{3}')".format(id, first_name, ccosto, clave)))
        cursor.commit()
        return json.dumps({'Respuesta': 'True'})
    except Exception as excep:
        return json.dumps({'Respuesta': 'False'})


def usuariosdelete(codigo):
    try:
        cursor = DATA_PROVIDER.conn.cursor()
        cursor.execute(generateDELETE(TABLE, "{0} {1} = '{2}'".format(WHERE, CODIGO, codigo)))
        cursor.commit()
        return json.dumps({'Respuesta': 'True'})
    except Exception as excep:
        return json.dumps({'Respuesta': 'False'})


def usuariosupdate(codigo):
    try:
        cursor = DATA_PROVIDER.conn.cursor()
        cursor.execute(generateUPDATE(TABLE, "{0} {1} = '{2}'".format(WHERE, CODIGO, codigo)))
        cursor.commit()
        return json.dumps({'Respuesta': 'True'})
    except Exception as excep:
        return json.dumps({'Respuesta': 'False'})

