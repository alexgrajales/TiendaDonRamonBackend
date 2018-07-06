from data_provider_service import DataProviderService

# db_engine = 'Driver={Pervasive ODBC Client Interface};ServerName=172.16.3.218;dbq=crmiclient;TCPPort=1583'
# db_engine = 'Driver={Pervasive ODBC Client Interface};ServerName=127.0.0.1;dbq=crmi;TCPPort=1583'
db_engine = 'Driver={Pervasive ODBC Client Interface};ServerName=127.0.0.1;dbq=TIENDA;TCPPort=1583'

DATA_PROVIDER = DataProviderService(db_engine)


def initialize_database():
    DATA_PROVIDER.init_database()
