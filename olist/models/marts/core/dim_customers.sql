{{ config(materialized='table') }}

select
    c.customer_id,
    c.customer_uid,
    c.zip_code_prefix,
    c.city as customer_city,
    c.state as customer_state,
    -- g.geo_lat as customer_lat,
    -- g.geo_lng as customer_lng,
    
    -- Customer metrics from orders
    co.total_orders,
    co.total_spent,
    co.avg_order_value,
    co.first_order_date,
    co.last_order_date,
    co.customer_segment,
    co.value_segment,
    co.customer_lifespan_days,
    co.delivery_success_rate,
    co.on_time_delivery_rate

from {{ ref('stg_customers') }} c
-- left join {{ ref('stg_geolocation') }} g 
    -- on c.zip_code_prefix = g.zip_code_prefix
left join {{ ref('int_customer_orders') }} co 
    on c.customer_id = co.customer_id