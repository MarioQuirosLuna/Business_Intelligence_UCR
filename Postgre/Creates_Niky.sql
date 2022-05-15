CREATE DATABASE Niky_Transactions

CREATE SCHEMA CUSTOMER
CREATE SCHEMA SALES
CREATE SCHEMA PRODUCTS

CREATE TABLE CUSTOMER.tb_Customers_Account
(
Customer_Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,First_Name VARCHAR(25) NOT NULL
,Last_Name VARCHAR(25) NULL
,Is_Deleted BIT DEFAULT('0') NOT NULL
,Registration_Date timestamp NOT NULL
)

CREATE TABLE CUSTOMER.tb_Email
(
Email_Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,Email VARCHAR(50) NOT NULL
,Is_Deleted BIT DEFAULT('0') NOT NULL
,Last_Modification timestamp NOT NULL
)

CREATE TABLE CUSTOMER.tb_Phone
(
Phone_Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,Country_Number VARCHAR(4) NOT NULL
,Phone_Number VARCHAR(9) NOT NULL
,Is_Deleted BIT DEFAULT('0') NOT NULL
,Last_Modification timestamp NOT NULL
)

CREATE TABLE CUSTOMER.tb_Credit_Card
(
Credit_Card_Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,Card_Number VARCHAR(16) NOT NULL
,Expiration_Month INT CHECK (Expiration_Month > 0 AND Expiration_Month < 13) NOT NULL
,Expiration_Year INT  CHECK (Expiration_Year > 2015) NOT NULL
,CW SMALLINT CHECK (CW > 99 AND CW < 1000) NOT NULL
,Is_Deleted BIT DEFAULT ('0') NOT NULL
,Last_Modification timestamp NOT NULL
)

CREATE TABLE CUSTOMER.tb_Customer_Email
(
Customer_Id INT NOT NULL
,Email_Id INT NOT NULL
,CONSTRAINT fk_CustomerEmail_Custo FOREIGN KEY (Customer_Id) REFERENCES CUSTOMER.tb_Customers_Account(Customer_Id)
,CONSTRAINT fk_CustomerEmail_Email FOREIGN KEY (Email_Id) REFERENCES CUSTOMER.tb_Email(Email_Id)
)

CREATE TABLE CUSTOMER.tb_Customer_Phone
(
Customer_Id INT NOT NULL
,Phone_Id INT NOT NULL
,CONSTRAINT fk_CustomerPhone_Custo FOREIGN KEY (Customer_Id) REFERENCES CUSTOMER.tb_Customers_Account(Customer_Id)
,CONSTRAINT fk_CustomerPhone_Phone FOREIGN KEY (Phone_Id) REFERENCES CUSTOMER.tb_Phone(Phone_Id)
)

CREATE TABLE CUSTOMER.tb_Customer_Card
(
Customer_Id INT NOT NULL
,Credit_Card_Id INT NOT NULL
,CONSTRAINT fk_CustomerCard_Custo FOREIGN KEY (Customer_Id) REFERENCES CUSTOMER.tb_Customers_Account(Customer_Id)
,CONSTRAINT fk_CustomerCard_Card FOREIGN KEY (Credit_Card_Id) REFERENCES CUSTOMER.tb_Credit_Card(Credit_Card_Id)
)

CREATE TABLE PRODUCTS.tb_Products
(
Product_Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,Name VARCHAR(30) NOT NULL
,Price NUMERIC(6,2) CHECK (Price > 0) NOT NULL
)

CREATE TABLE SALES.Sales_Head
(
Sales_Head_Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,Customer_id INT NOT NULL
,Credit_Card_Id INT NULL
,Paid_In_Cash BIT NOT NULL DEFAULT('0')
,Total_Price NUMERIC(9,2) CHECK (Total_Price > 0) NOT NULL
,Date_Of_Sale timestamp NOT NULL
,CONSTRAINT fk_SalesCard FOREIGN KEY (Credit_Card_Id) REFERENCES CUSTOMER.tb_Credit_Card(Credit_Card_Id)
,CONSTRAINT fk_SalesCustomer FOREIGN KEY (Customer_id) REFERENCES CUSTOMER.tb_Customers_Account(Customer_Id)
)

CREATE TABLE SALES.Sales_Detail
( 
Sales_Head_Id INT NOT NULL
,Sales_Detail_Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
,Product_Id INT NOT NULL
,Number_Of_Products INT NOT NULL
,SubTotal_Price NUMERIC(9,2) CHECK (SubTotal_Price > 0) NOT NULL
,CONSTRAINT fk_SalesHead_Id FOREIGN KEY (Sales_Head_Id) REFERENCES SALES.Sales_Head(Sales_Head_Id)
,CONSTRAINT fk_SalesDetail_Product FOREIGN KEY (Product_Id) REFERENCES PRODUCTS.tb_Products(Product_Id)
)

