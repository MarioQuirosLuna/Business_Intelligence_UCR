-- =============================================
-- Description:	Elimina las tablas para reestablecerlas
-- =============================================
CREATE PROCEDURE sp_DropTables
AS
BEGIN
	IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[SALES].[FACT_SALES]') AND type in (N'U'))
	BEGIN
		DROP TABLE [SALES].[FACT_SALES];
	END
	IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[SALES].[DIM_Products]') AND type in (N'U'))
	BEGIN
		DROP TABLE [SALES].[DIM_Products];
	END
	IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[SALES].[DIM_Sales_Head]') AND type in (N'U'))
	BEGIN
		DROP TABLE [SALES].[DIM_Sales_Head];
	END
END
GO

USE [IF5100_2022_B76090]
GO

/****** Object:  Table [FINANCIAL_DEPOSIT].[tb_EVENTS]    Script Date: 15/05/2022 8:05:59 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[FINANCIAL_DEPOSIT].[tb_EVENTS]') AND type in (N'U'))
DROP TABLE [FINANCIAL_DEPOSIT].[tb_EVENTS]
GO

