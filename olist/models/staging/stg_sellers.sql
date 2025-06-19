{{ config(materialized='view') }}

select
    seller_id,
    zip_code_prefix,
    city,
    state,
    current_timestamp() as _loaded_at
from {{ source('olist', 'sellers') }}