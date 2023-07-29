-- Retrieve the top 5 customers who have made the highest average order amounts in the last 6 months:


SELECT c.customer_id, c.customer_name, AVG(o.order_amount) AS avg_order_amount
FROM Customers c
JOIN (
    SELECT customer_id, order_id, SUM(price) AS order_amount
    FROM Orders o
    JOIN Prices p ON o.product_id = p.product_id AND o.variant_id = p.variant_id
    WHERE order_date >= DATE('now', '-6 months')
    GROUP BY customer_id, order_id
) o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY avg_order_amount DESC
LIMIT 5;
