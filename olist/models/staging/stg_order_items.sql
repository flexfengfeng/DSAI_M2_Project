{{ config(materialized='view') }}

select
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value,
    current_timestamp() as _loaded_at
from {{ source('olist', 'order_items') }}