CREATE TABLE Persons(PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255), City varchar(255))
insert into Persons(PersonID, LastName, FirstName, Address, City) VALUES(26921, 'duguru', 'Ushasri', 'kukatpally', 'Hyderabad')
insert into Persons(personid, lastname, firstname, address, city) VALUES(21394, 'sinjalapuram', 'Ramu', 'muntimadugu', 'anantapur')
DELETE from Persons where personid = 8971
SELECT * FROM Persons
insert into persons(personid, lastname, firstname, address, city) VALUES(8791, 'duguru', 'Venkatesh', 'Tadipatri', 'anantapu')
SELECT count(*) from Persons where lastname = 'duguru'
ALTER TABLE Persons DROP id
DELETE from Persons where personid = NULL
CREATE TABLE OrderDetails(OrderDetailID int, OrderID int, ProductID int, Quantity int, ProductName VARCHAR(100))
select * from OrderDetails
insert into OrderDetails(orderdetailid, orderid, productid, quantity, productname) values(5, 10249, 51, 40, 'Sheets')
SELECT sum(Quantity)
FROM OrderDetails
WHERE ProductID = 11;
ALTER TABLE OrderDetails Drop productname
select sum(Quantity)
from OrderDetails where productid = 11
ALTER TABLE OrderDetails ADD ProductName VARCHAR(100)
SELECT SUM(quantity) AS TOTAL FROM OrderDetails
SELECT orderid, SUM(quantity) AS [TOTAL QUANTITY]
FROM OrderDetails GROUP BY orderid
SELECT SUM(QUANTITY * 10)
FROM OrderDetails
SELECT SUM(quantity) FROM OrderDetails
SELECT SUM(quantity) FROM OrderDetails WHERE productid IS 11
SELECT SUM(quantity) FROM OrderDetails WHERE productid = 11
