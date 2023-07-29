-- Retrieve the list of customer whose order value is lower this year as compared to previous year

SELECT c.customer_id, c.customer_name
FROM Customers c
JOIN (
    SELECT customer_id, order_id, SUM(price) AS order_amount
    FROM Orders o
    JOIN Prices p ON o.product_id = p.product_id AND o.variant_id = p.variant_id
    WHERE order_date >= DATE('now', '-2 years') AND order_date < DATE('now', '-1 years')
    GROUP BY customer_id, order_id
) prev_year ON c.customer_id = prev_year.customer_id
JOIN (
    SELECT customer_id, order_id, SUM(price) AS order_amount
    FROM Orders o
    JOIN Prices p ON o.product_id = p.product_id AND o.variant_id = p.variant_id
    WHERE order_date >= DATE('now', '-1 years')
    GROUP BY customer_id, order_id
) this_year ON c.customer_id = this_year.customer_id
WHERE this_year.order_amount < prev_year.order_amount;
