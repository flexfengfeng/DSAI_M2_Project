{{ config(materialized='table') }}

select
    customer_state,
    customer_city,
    customer_segment,
    value_segment,
    
    count(*) as customer_count,
    sum(total_orders) as total_orders,
    sum(total_spent) as total_revenue,
    avg(avg_order_value) as avg_order_value,
    avg(customer_lifespan_days) as avg_customer_lifespan,
    avg(delivery_success_rate) as avg_delivery_success_rate,
    avg(on_time_delivery_rate) as avg_on_time_delivery_rate,
    
    -- Customer distribution
    count(*) / sum(count(*)) over() as customer_share,
    sum(total_spent) / sum(sum(total_spent)) over() as revenue_share

from {{ ref('dim_customers') }}
where total_orders is not null
group by 1,2,3,4