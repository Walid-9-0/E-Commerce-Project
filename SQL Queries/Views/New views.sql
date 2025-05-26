CREATE VIEW DimCustomer AS
SELECT 
    id AS customer_id,
    CONCAT(first_name, ' ',last_name ) AS full_name,
    LTRIM(RTRIM(SUBSTRING(
        address,
        CHARINDEX(',', address) + 1,
        CHARINDEX(' ', address, CHARINDEX(',', address) + 2) - CHARINDEX(',', address) - 1
    ))) AS state,
    registration_date
FROM Customers;


----------------------------------------------

CREATE VIEW DimProduct AS
SELECT 
    p.id AS product_id,
    p.name AS product_name,
    p.price,
    p.stock_quantity,
	c.id AS category_id,
    c.name AS category_name,
    s.name AS supplier_name,
    LTRIM(RTRIM(SUBSTRING(s.address, 
      CHARINDEX(',', address) + 1,         
      CHARINDEX(' ', address, CHARINDEX(',', address) + 2) - CHARINDEX(',', address) - 1
  ))) AS suppliers_state
FROM Products p
LEFT JOIN Categories c ON p.category_id = c.id
LEFT JOIN Suppliers s ON p.supplier_id = s.id;


------------------------------------------------

CREATE VIEW FactOrders AS
SELECT 
    o.id AS order_id,
    o.customer_id,
    o.order_date,
    od.product_id,
    od.quantity,
    od.unit_price,
	(od.quantity * od.unit_price) as revenue  ,
    o.total_amount,
    o.status AS order_status,
    d.percentage AS discount_percentage
FROM Orders o
JOIN [dbo].[order_details] od ON o.id = od.order_id
LEFT JOIN Discounts d ON od.product_id = d.product_id;


---------------------------------------------------------


CREATE VIEW FactPayments AS
SELECT 
    id AS payment_id,
    order_id,
    customer_id,
    amount,
    payment_date,
    payment_method,
    status
FROM Payments;


--------------------------------------------
CREATE VIEW FactShipping AS
SELECT 
    id AS shipping_id,
    order_id,
    shipping_date,
    carrier,
    status AS shipping_status
FROM Shipping



-----------------------------------------

CREATE VIEW FactReturns AS
SELECT 
    id AS return_id,
    order_id,
    return_date,
    reason,
    status AS return_status
FROM Returns;


---------------------------------
CREATE VIEW FactWishlist AS
SELECT 
    id AS wishlist_id,
    customer_id,
    product_id,
    added_date
FROM Wishlists;

--------------------------------

CREATE VIEW FactInventoryMovements AS
SELECT 
    id AS movement_id,
    product_id,
    quantity,
    movement_type,
    movement_date
FROM [dbo].[inventory_movements];

-----------------------------------

CREATE VIEW FactCustomerSessions AS
SELECT 
    id AS session_id,
    customer_id,
    session_start,
    session_end,
    DATEDIFF(MINUTE, session_start, session_end) AS session_length
FROM customer_sessions;


