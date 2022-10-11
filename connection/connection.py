import pyodbc


def get_cnxn() -> pyodbc.Connection:
    server = 'localhost'
    database = 'jogos'
    username = 'sa'
    password = 'root'
    with pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as cnxn:
        return cnxn
