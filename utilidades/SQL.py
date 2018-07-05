import utilidades.Const
import uuid

SENTENCIAS = [utilidades.Const.INSERT, utilidades.Const.UPDATE, utilidades.Const.SELECT, utilidades.Const.DELETE]


def generateUnicId(size):
    return str(uuid.uuid4().fields[-1])[:size]

def generateSELECT(table, listColums=None, all=False, query=None):
    """

    :type query: object
    """
    respuesta = None
    if all:
        respuesta = '{0} {1} {2} {3}'.format(utilidades.Const.SELECT, utilidades.Const.ALL, utilidades.Const.FROM, table);
    elif listColums != None:
        respuesta = '{0} {1} {2} {3}'.format(utilidades.Const.SELECT, listColums, utilidades.Const.FROM, table);

    if query != None:
        respuesta += query
    return respuesta


def generateINSERT(table=None, listColums=None, listValues=None):
    respuesta = None

    return '{0} {1} {2} {3} {4} {5}'.format(utilidades.Const.INSERT, utilidades.Const.INTO, table, listColums,
                                         utilidades.Const.VALUES, listValues)


def generateDELETE(table=None, query=None):
    respuesta = None

    return '{0} {1} {2} {3}'.format(utilidades.Const.DELETE, utilidades.Const.FROM, table, query)


def generateUPDATE(table=None, columsAndValues=None,query=None):
    respuesta = None

    return '{0} {1} {2} {3} {4}'.format(utilidades.Const.UPDATE, table, utilidades.Const.SET, columsAndValues, query)