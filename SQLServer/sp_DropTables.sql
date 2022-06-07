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
	IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[SALES].[DIM_DATES]') AND type in (N'U'))
	BEGIN
		DROP TABLE [SALES].[DIM_DATES];
	END
	IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[SALES].[DIM_Payment_Method]') AND type in (N'U'))
	BEGIN
		DROP TABLE [SALES].[DIM_Payment_Method];
	END
END
GO

