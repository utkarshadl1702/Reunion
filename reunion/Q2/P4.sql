
--Retrieve the list of top 5 selling products. Further bifurcate the sales by product variants

SELECT p.product_id, p.product_name, v.variant_name, COUNT(o.order_id) AS total_sales
FROM Products p
LEFT JOIN Variants v ON p.product_id = v.product_id
LEFT JOIN Prices pr ON p.product_id = pr.product_id AND v.variant_id = pr.variant_id
LEFT JOIN Orders o ON pr.product_id = o.product_id AND pr.variant_id = o.variant_id
GROUP BY p.product_id, p.product_name, v.variant_name
ORDER BY total_sales DESC
LIMIT 5;
