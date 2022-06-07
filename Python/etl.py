from decouple import config
from datetime import datetime
import psycopg2
import pyodbc
import csv
import os


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


def connectSQLServerLocal():
    return pyodbc.connect('DRIVER={SQL Server};SERVER='+config('SQLSERVER_HOST_LOCAL')+';DATABASE='+config('SQLSERVER_DATABASE_LOCAL')+';Trusted_Connection=yes;')


def getProducts(cursorPosgreSQL):
    query = "SELECT Product_Id, Name, Price FROM PRODUCTS.tb_Products"
    cursorPosgreSQL.execute(query)
    products = cursorPosgreSQL.fetchall()

    with open('products.csv', 'w') as csvProducts:
        fieldnames = ['Product_Id', 'Name', 'Price']
        writer = csv.DictWriter(csvProducts, fieldnames=fieldnames)
        writer.writeheader()
        for aux in products:
            writer.writerow(
                {'Product_Id': aux[0], 'Name': aux[1], 'Price': aux[2]})


def addDescription(val):
    if val == '1':
        return "Cash"
    else:
        return "Credit Card"


def getSalesHead(cursorPosgreSQL):
    query = "SELECT Sales_Head_Id, Paid_In_Cash FROM SALES.Sales_Head"
    cursorPosgreSQL.execute(query)
    sales = cursorPosgreSQL.fetchall()

    with open('sales.csv', 'w') as csvSales:
        fieldnames = ['Sales_Head_id', 'Paid_In_Cash', 'Paid_Type_Description']
        writer = csv.DictWriter(csvSales, fieldnames=fieldnames)
        writer.writeheader()
        for aux in sales:
            writer.writerow(
                {'Sales_Head_id': aux[0], 'Paid_In_Cash': aux[1], 'Paid_Type_Description': addDescription(aux[1])})


def getDates(cursorPosgreSQL):
    query = "SELECT Sales_Head_Id, Date_Of_Sale FROM SALES.Sales_Head"
    cursorPosgreSQL.execute(query)
    dates = cursorPosgreSQL.fetchall()

    with open('dates.csv', 'w') as csvDates:
        fieldnames = ['Sales_Head_Date_id',
                      'Date_Of_Sale', 'Date_Year', 'Date_Month']
        writer = csv.DictWriter(csvDates, fieldnames=fieldnames)
        writer.writeheader()
        for aux in dates:
            writer.writerow(
                {'Sales_Head_Date_id': aux[0], 'Date_Of_Sale': aux[1], 'Date_Year': aux[1].strftime('%Y'), 'Date_Month': aux[1].strftime('%m')})


def getFactData(cursorPosgreSQL):
    query = "SELECT SD.Product_Id, SH.Sales_Head_Id, SD.Number_Of_Products, SD.SubTotal_Price, SH.Total_Price FROM SALES.Sales_Head AS SH INNER JOIN SALES.Sales_Detail AS SD ON SH.Sales_Head_Id = SD.Sales_Head_Id"
    cursorPosgreSQL.execute(query)
    facts = cursorPosgreSQL.fetchall()

    with open('facts.csv', 'w') as csvFacts:
        fieldnames = ['Id', 'Product_id', 'Sales_Head_id', 'Sales_Head_Date_id',
                      'Amount_Of_Sales', 'SubTotal_Price', 'Total_Price']
        writer = csv.DictWriter(csvFacts, fieldnames=fieldnames)

        writer.writeheader()
        count = 0
        for aux in facts:
            writer.writerow(
                {'Id': count, 'Product_id': aux[0], 'Sales_Head_id': aux[1], 'Sales_Head_Date_id': aux[1],
                 'Amount_Of_Sales': aux[2], 'SubTotal_Price': aux[3], 'Total_Price': aux[4]})
            count += 1


def dropTables(cursorSQLServer):
    query = 'EXEC sp_DropTables;'
    cursorSQLServer.execute(query)
    print("Drop tables successfully")


def createTables(cursorSQLServer):
    query = 'EXEC sp_CreateTables'
    cursorSQLServer.execute(query)
    print("Create table DIM_Products, DIM_Payment_Method, DIM_Dates, FACT_SALES successfully")


def loadDIMProducts(cursorSQLServer):
    query = "BULK INSERT SALES.DIM_Products FROM '"+os.path.dirname(os.path.abspath(
        __file__))+"\\products.csv' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')"
    cursorSQLServer.execute(query)
    cursorSQLServer.commit()
    print("Products load successfully")


def loadDIMSalesHead(cursorSQLServer):
    query = "BULK INSERT SALES.DIM_Payment_Method FROM '"+os.path.dirname(os.path.abspath(
        __file__))+"\\sales.csv' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')"
    cursorSQLServer.execute(query)
    cursorSQLServer.commit()
    print("Payment Method load successfully")


def loadDIMDates(cursorSQLServer):
    query = "BULK INSERT SALES.DIM_Dates FROM '"+os.path.dirname(os.path.abspath(
        __file__))+"\\dates.csv' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')"
    cursorSQLServer.execute(query)
    cursorSQLServer.commit()
    print("Dates load successfully")


def loadDIMFactData(cursorSQLServer):
    query = "BULK INSERT SALES.FACT_SALES FROM '"+os.path.dirname(os.path.abspath(
        __file__))+"\\facts.csv' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')"
    cursorSQLServer.execute(query)
    cursorSQLServer.commit()
    print("Fact load successfully")


try:
    connectionPostgreSQL = connectPosgreSQL()
    print('Connection successfully to PosgreSQL')
    with connectionPostgreSQL.cursor() as cursorPosgreSQL:
        print(
            "\n*****************************\n Extract data in progress...\n*****************************\n")
        getProducts(cursorPosgreSQL)
        getSalesHead(cursorPosgreSQL)
        getDates(cursorPosgreSQL)
        getFactData(cursorPosgreSQL)

        #connectionSQLServer = connectSQLServer()
        connectionSQLServer = connectSQLServerLocal()
        print('Connection successfully to SQLServer')

        with connectionSQLServer.cursor() as cursorSQLServer:
            dropTables(cursorSQLServer)

            createTables(cursorSQLServer)

            print(
                "\n*****************************\n Load data in progress...\n*****************************\n")
            loadDIMProducts(cursorSQLServer)
            loadDIMSalesHead(cursorSQLServer)
            loadDIMDates(cursorSQLServer)
            loadDIMFactData(cursorSQLServer)

            print(
                "\n*****************************\n Load data successfully!!\n*****************************\n")

except Exception as ex:
    print("Error with connection ", ex)
finally:
    print("Connection close")
    connectionPostgreSQL.close()
    connectionSQLServer.close()
