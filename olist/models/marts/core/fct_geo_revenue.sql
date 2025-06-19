{{
  config(
    materialized='table',
    cluster_by = ['state', 'city']
  )
}}

WITH orders AS (
  SELECT 
    order_id, 
    customer_id
  FROM `brazil-olist.Olist.orders`
  WHERE order_status = 'delivered'  -- 只考虑已交付订单
),

payments AS (
  SELECT
    order_id,
    SUM(payment_value) AS total_revenue
  FROM `brazil-olist.Olist.order_payments`
  GROUP BY 1
),

customers AS (
  SELECT
    customer_id,
    zip_code_prefix
  FROM `brazil-olist.Olist.customer`
)

SELECT
  geo.zip_code_prefix,
  geo.avg_latitude,
  geo.avg_longitude,
  geo.city,
  geo.state,
  SUM(p.total_revenue) AS total_revenue,
  COUNT(DISTINCT o.order_id) AS order_count
FROM orders o
JOIN payments p ON o.order_id = p.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN {{ ref('stg_geolocation_map') }} geo 
  ON c.zip_code_prefix = geo.zip_code_prefix
GROUP BY 1,2,3,4,5