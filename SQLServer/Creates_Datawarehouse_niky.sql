CREATE DATABASE IF5100_2022_DATAWAREHOUSE_NIKY

USE IF5100_2022_DATAWAREHOUSE_NIKY

CREATE SCHEMA SALES
exec [dbo].[sp_DropTables]
CREATE TABLE SALES.DIM_Products
(
	Product_id INT PRIMARY KEY NOT NULL,
	Name VARCHAR(30) NOT NULL,
	Amount_Of_Sales INT NOT NULL DEFAULT(0),
	Price NUMERIC(6,2) NOT NULL
)

CREATE TABLE SALES.DIM_Sales_Head
(
	Sales_Head_id INT PRIMARY KEY NOT NULL,
	Paid_In_Cash BIT NOT NULL,
	Paid_Type_Description VARCHAR(50) NOT NULL,
	Date_Of_Sale DATETIME NOT NULL
)

CREATE TABLE SALES.FACT_SALES
(
	Id INT PRIMARY KEY NOT NULL,
	Product_id INT NOT NULL,
	Sales_Head_id INT NOT NULL,
	SubTotal_Price NUMERIC(9,2) NOT NULL,
	Total_Price NUMERIC(9,2) NOT NULL,
	FOREIGN KEY (Product_id) REFERENCES SALES.DIM_Products(Product_id),
	FOREIGN KEY (Sales_Head_id) REFERENCES SALES.DIM_Sales_Head(Sales_Head_id)
)

select * from SALES.DIM_Products
order by Amount_Of_Sales Desc

select * from SALES.DIM_Sales_Head