{{ config(materialized='view') }}

select
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value,
    current_timestamp() as _loaded_at
from {{ source('olist', 'order_payments') }}