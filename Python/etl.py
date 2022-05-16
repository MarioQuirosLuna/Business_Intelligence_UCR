from decouple import config
from datetime import datetime
import psycopg2
import pyodbc


def connectPosgreSQL():
    return psycopg2.connect(
        host=config('POSGRESQL_HOST'),
        user=config('POSGRESQL_USER'),
        password=config('POSGRESQL_PASS'),
        database=config('POSGRESQL_DATABASE')
    )


def connectSQLServer():
    return pyodbc.connect(
        'DRIVER={SQL Server};SERVER='+config('SQLSERVER_HOST')+';DATABASE='+config(
            'SQLSERVER_DATABASE')+';UID='+config('SQLSERVER_USER')+';PWD='+config('SQLSERVER_PASS')
    )


def getProducts(cursorPosgreSQL):
    query = "SELECT Product_Id, Name, Price FROM PRODUCTS.tb_Products"
    cursorPosgreSQL.execute(query)
    return cursorPosgreSQL.fetchall()


def getSalesHead(cursorPosgreSQL):
    query = "SELECT Sales_Head_Id, Paid_In_Cash FROM SALES.Sales_Head"
    cursorPosgreSQL.execute(query)
    return cursorPosgreSQL.fetchall()


def dropTables(cursorSQLServer):
    query = 'EXEC sp_DropTables;'
    cursorSQLServer.execute(query)
    print("Drop tables successfull")


def createTables(cursorSQLServer):
    query = 'EXEC sp_CreateTables'
    cursorSQLServer.execute(query)
    print("Create table DIM_Products, DIM_Sales_Head, FACT_SALES successfull")


def loadDIMProducts(cursorSQLServer, products):
    for aux in products:
        query = 'INSERT INTO SALES.DIM_Products VALUES(?,?,?);'
        cursorSQLServer.execute(
            query, (aux[0], aux[1], aux[2]))


def addDescription(val):
    if val == '1':
        return "Cash"
    else:
        return "Credit Card"


def loadDIMSalesHead(cursorSQLServer, salesHead):
    for aux in salesHead:
        query = 'INSERT INTO SALES.DIM_Sales_Head VALUES(?,?,?);'
        cursorSQLServer.execute(
            query, (aux[0], aux[1], addDescription(aux[1])))
        if aux[0] == 50: #break for testing
            break
        print(aux[0])


try:
    connectionPostgreSQL = connectPosgreSQL()
    print('Connection successfully to PosgreSQL')
    with connectionPostgreSQL.cursor() as cursorPosgreSQL:
        print(
            "\n*****************************\n Extract data in progress...\n*****************************\n")
        products = getProducts(cursorPosgreSQL)
        salesHead = getSalesHead(cursorPosgreSQL)

        connectionSQLServer = connectSQLServer()
        print('Connection successfully to SQLServer')

        with connectionSQLServer.cursor() as cursorSQLServer:
            dropTables(cursorSQLServer)

            createTables(cursorSQLServer)

            print(
                "\n*****************************\n Load data in progress...\n*****************************\n")
            loadDIMProducts(cursorSQLServer, products)
            loadDIMSalesHead(cursorSQLServer, salesHead)

            print("Load data successfull")

except Exception as ex:
    print("Error with connection ", ex)
finally:
    print("Connection close")
    connectionPostgreSQL.close()
    connectionSQLServer.close()
