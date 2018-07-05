from middleware import DATA_PROVIDER
from const_clientes import *
from const import *
import json
import MySQLdb
from flask import request
from utilidades.SQL import *
import utilidades.Const

def clientes():
    cursor = DATA_PROVIDER.conn.cursor()
    cursor.execute(SELECTCLIENTE)
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps(query_result)


def cliente(codigo):
    cursor = DATA_PROVIDER.conn.cursor()
    query = '{} {} "{}" = {}'.format(SELECTCLIENTE, WHERE, CODIGOCLIENTE, codigo)
    cursor.execute(query)
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps(query_result)



def montajes():
    cursor = DATA_PROVIDER.conn.cursor()
    cursor.execute(SELECTMONTAJES)
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps(query_result)


def revisarcleardb():
    cambiaron = 0;
    igual = 1
    lista = []
    datacleardb = conexion_sql('SELECT * FROM paginaweb.aplicaciones_aplicacioncliente', 'us-cdbr-azure-east-c.cloudapp.net', 'b06c7b01b88d65', 'f38f8153', 'paginaweb', '3306')
    datamysqlazure = conexion_sql('SELECT * FROM paginaweb.aplicaciones_aplicacioncliente', 'paginaweb.mysql.database.azure.com', 'appweb.support@paginaweb', 'Med1ris1ltd@.', 'paginaweb', '3306')
    for recorrido in datacleardb:
        for recorridodos in datamysqlazure:
            if recorrido[0] == recorridodos[0]:
                if recorridodos <> recorrido:
                    cambiaron = cambiaron +1
                    lista.append(str(recorridodos[1]) + "," + str(recorridodos[2]))
                    query = 'update paginaweb.aplicaciones_aplicacioncliente set estado="'+recorrido[3]+'"'+', activo="'+recorrido[4]+'"'+', fechafinal="'+str(recorrido[6])+'"'+', fechainicial="'+str(recorrido[5])+'"'+' where codigo_aplicacion_id="'+recorrido[1]+'"'+' and codigo_cliente_id="'+recorrido[2]+'"'
                    b = conexion_sql(query, 'paginaweb.mysql.database.azure.com', 'appweb.support@paginaweb', 'Med1ris1ltd@.', 'paginaweb', '3306')
                    print "cambio"
                else:
                    igual = igual +1
                # datamysqlazure.pop(datamysqlazure.index(recorridodos))
                break
    print "cambiaron " + str(cambiaron)
    print "no cambiaron " + str(igual)
    for rec in lista:
        print rec
    # cursor = DATA_PROVIDER.conn.cursor()
    # query = '{} {} "{}" = {}'.format(SELECTCLIENTE, WHERE, CODIGOCLIENTE, codigo)
    # cursor.execute(query)
    # query_result = [dict(line) for line in
    #                 [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return json.dumps('')


def conexion_sql(query, host, user, password, name, port):
    datos = [host, user,
             password, name,
             int(port)]
    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)
    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Traer los resultados de un select
    else:
        conn.commit()  # Hacer efectiva la escritura de datos
        data = None
    cursor.close()
    conn.close()
    if query.upper().startswith('SELECT'):
        return list(data)
    else:
        return data