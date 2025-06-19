{{
  config(
    materialized='view'
  )
}}

SELECT
  order_id,
  customer_id,
  TIMESTAMP_DIFF(
    order_delivered_customer_date, 
    order_delivered_carrier_date, 
    HOUR
  ) AS delivery_hours
FROM `brazil-olist.Olist.orders`
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_delivered_carrier_date IS NOT NULL
  AND order_delivered_customer_date >= order_delivered_carrier_date