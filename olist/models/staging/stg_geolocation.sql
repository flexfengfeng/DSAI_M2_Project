{{ config(materialized='view') }}

select
    zip_code_prefix,
    geo_lat,
    geo_lng,
    city,
    state,
    current_timestamp() as _loaded_at
from {{ source('olist', 'geolocation') }}