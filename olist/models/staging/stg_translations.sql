{{ config(materialized='view') }}

select
    product_category_name,
    product_category_name_english,
    current_timestamp() as _loaded_at
from {{ source('olist', 'translations') }}