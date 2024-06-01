create database final;

--create customer table
CREATE TABLE Customer (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10), -- Assuming gender can be any string, adjust as needed
    address VARCHAR(255),
    password VARCHAR(max),
);


select * from Customer



--create productTable
CREATE TABLE ProductTable1 (
    productID INT IDENTITY(1,1) PRIMARY KEY,
    productName VARCHAR(50),
    prdouctPrice INT,
    ProductDesc VARCHAR(150),
	image_path VARCHAR(255),

);


select * from ProductTable1

--ALTER TABLE ProductTable1
--ADD image_path VARCHAR(255); -- Adjust the length as needed


-- Create Order table
CREATE TABLE OrderTable (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    cust_id INT FOREIGN KEY REFERENCES Table_1(id),
    order_date DATE DEFAULT GETDATE(), -- only date without time
	totalPrice int,
);
select * from OrderTable

---

-- Create OrderDetails with composite primary key
CREATE TABLE OrderDetails (
    order_id INT FOREIGN KEY REFERENCES OrderTable(order_id),
    product_id INT FOREIGN KEY REFERENCES ProductTable1(productID),
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);
GO

SELECT * FROM OrderDetails;
GO


--employee table:
create table empTable(
	empID INT IDENTITY(1,1) PRIMARY KEY,
	empName VARCHAR(50),
    age INT,
	empSalary int,
);

insert into empTable values('ahmed',23,100, '2023-04-27', '2024-04-27')
insert into empTable values('ali',23,300, '2023-05-15', null)

select * from empTable


-- revenue code 
/*
CREATE PROCEDURE sp_revenueOf
    @days INT = 1
AS
BEGIN
    DECLARE @i INT = 0;
    DECLARE @today DATE = CAST(GETDATE() AS DATE);
    DECLARE @currentDate DATE;
    DECLARE @dailyGrossIncome DECIMAL(10, 2);
    DECLARE @dailyExpenses DECIMAL(10, 2);
    DECLARE @table TABLE ([Dates] DATE, [Gross Income] DECIMAL(10, 2), [Expenses] DECIMAL(10, 2), [Net Revenue] DECIMAL(10, 2));

    WHILE @i < @days
    BEGIN
        SET @currentDate = DATEADD(DAY, -@i, @today);
        SELECT @dailyGrossIncome = ISNULL(SUM(dbo.OrderTable.totalPrice), 0)
        FROM OrderTable
        WHERE order_date = @currentDate;
        SELECT @dailyExpenses = ISNULL(SUM(dbo.empTable.empSalary), 0)
        FROM empTable
        WHERE @currentDate BETWEEN startDate AND ISNULL(endDate, '9999-12-31');
        INSERT INTO @table VALUES (@currentDate, @dailyGrossIncome, @dailyExpenses, @dailyGrossIncome - @dailyExpenses);
        SET @i = @i + 1;
    END
    SELECT * FROM @table;
END;
*/

select * from ProductTable1

exec sp_revenueOf @days = 17