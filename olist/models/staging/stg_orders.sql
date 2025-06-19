{{ config(materialized='view') }}

select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date,
    current_timestamp() as _loaded_at
from {{ source('olist', 'orders') }}