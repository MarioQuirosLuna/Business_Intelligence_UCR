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


def getDates(cursorPosgreSQL):
    query = "SELECT Sales_Head_Id, Date_Of_Sale FROM SALES.Sales_Head"
    cursorPosgreSQL.execute(query)
    return cursorPosgreSQL.fetchall()


def getFactData(cursorPosgreSQL):
    query = "SELECT SD.Product_Id, SH.Sales_Head_Id, SD.Number_Of_Products, SD.SubTotal_Price, SH.Total_Price FROM SALES.Sales_Head AS SH INNER JOIN SALES.Sales_Detail AS SD ON SH.Sales_Head_Id = SD.Sales_Head_Id"
    cursorPosgreSQL.execute(query)
    return cursorPosgreSQL.fetchall()


def dropTables(cursorSQLServer):
    query = 'EXEC sp_DropTables;'
    cursorSQLServer.execute(query)
    print("Drop tables successfully")


def createTables(cursorSQLServer):
    query = 'EXEC sp_CreateTables'
    cursorSQLServer.execute(query)
    print("Create table DIM_Products, DIM_Sales_Head, DIM_Dates, FACT_SALES successfully")


def loadDIMProducts(cursorSQLServer, products):
    for aux in products:
        query = 'INSERT INTO SALES.DIM_Products VALUES(?,?,?);'
        cursorSQLServer.execute(
            query, (aux[0], aux[1], aux[2]))
    print("Products load successfully")


def addDescription(val):
    if val == '1':
        return "Cash"
    else:
        return "Credit Card"


def loadDIMSalesHead(cursorSQLServer, salesHead):
    count = 0
    for aux in salesHead:
        query = 'INSERT INTO SALES.DIM_Sales_Head VALUES(?,?,?);'
        cursorSQLServer.execute(
            query, (aux[0], aux[1], addDescription(aux[1])))
        count += 1
        print("Sales Head ", count)
        # if count == 55:  # break for testing
        #    break
    print("SalesHead load successfully")


def loadDIMDates(cursorSQLServer, dates):
    count = 0
    for aux in dates:
        query = 'INSERT INTO SALES.DIM_DATES VALUES(?,?,?,?)'
        cursorSQLServer.execute(
            query, (aux[0], aux[1], aux[1].strftime('%Y'), aux[1].strftime('%m')))
        count += 1
        print("Date ", count)
        # if count == 50:  # break for testing
        #    break
    print("Dates load successfully")


def loadDIMFactData(cursorSQLServer, factData):
    count = 0
    for aux in factData:
        query = 'INSERT INTO SALES.FACT_SALES VALUES(?,?,?,?,?,?,?)'
        cursorSQLServer.execute(
            query, (count, aux[0], aux[1], aux[1], aux[2], aux[3], aux[4]))
        count += 1
        print("Fact ", count)
    print("Fact load successfully")


try:
    connectionPostgreSQL = connectPosgreSQL()
    print('Connection successfully to PosgreSQL')
    with connectionPostgreSQL.cursor() as cursorPosgreSQL:
        print(
            "\n*****************************\n Extract data in progress...\n*****************************\n")
        products = getProducts(cursorPosgreSQL)
        salesHead = getSalesHead(cursorPosgreSQL)
        dates = getDates(cursorPosgreSQL)
        factData = getFactData(cursorPosgreSQL)

        connectionSQLServer = connectSQLServer()
        print('Connection successfully to SQLServer')

        with connectionSQLServer.cursor() as cursorSQLServer:
            dropTables(cursorSQLServer)

            createTables(cursorSQLServer)

            print(
                "\n*****************************\n Load data in progress...\n*****************************\n")
            loadDIMProducts(cursorSQLServer, products)
            loadDIMSalesHead(cursorSQLServer, salesHead)
            loadDIMDates(cursorSQLServer, dates)
            loadDIMFactData(cursorSQLServer, factData)

            print("Load data successfully")

except Exception as ex:
    print("Error with connection ", ex)
finally:
    print("Connection close")
    connectionPostgreSQL.close()
    connectionSQLServer.close()
