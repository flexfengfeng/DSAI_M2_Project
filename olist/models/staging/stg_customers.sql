{{ config(materialized='view') }}

select
    customer_id,
    customer_uid,
    zip_code_prefix,
    city,
    state,
    current_timestamp() as _loaded_at
from {{ source('olist', 'customer') }}