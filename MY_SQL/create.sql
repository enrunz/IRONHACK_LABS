CREATE TABLE Cars(VIN VARCHAR(20) PRIMARY KEY, make VARCHAR(15), model VARCHAR(20), year TINYINT(4), color CHAR(10));
CREATE TABLE Customers(customer_id CHAR(6) PRIMARY KEY, name VARCHAR(40), phone VARCHAR(14), email VARCHAR(40), address VARCHAR(40), city CHAR(15), state VARCHAR(20), postal VARCHAR(10));
CREATE TABLE Salesperson(staff_id CHAR(5) PRIMARY KEY, name VARCHAR(40), store VARCHAR(40));
CREATE TABLE Invoices(invoice_id CHAR(9) PRIMARY KEY, date DATETIME, VIN VARCHAR(20), customer_id CHAR(6),staff_id CHAR(5));