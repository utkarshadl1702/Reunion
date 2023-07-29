-- Create a table showing cumulative purchase by a particular customer. Show the breakup of cumulative purchases by product category:

CREATE VIEW CumulativePurchase AS
SELECT c.customer_id, c.customer_name, p.product_name, v.variant_name, SUM(price) AS cumulative_purchase
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Prices pr ON o.product_id = pr.product_id AND o.variant_id = pr.variant_id
JOIN Products p ON pr.product_id = p.product_id
LEFT JOIN Variants v ON pr.variant_id = v.variant_id
GROUP BY c.customer_id, c.customer_name, p.product_name, v.variant_name
ORDER BY c.customer_id, p.product_name, v.variant_name;


--CumulativePurchase view to get the cumulative purchase by a particular customer, broken down by product category:
SELECT customer_id, customer_name, product_name, variant_name, cumulative_purchase
FROM CumulativePurchase
WHERE customer_id = <customer_id>;
