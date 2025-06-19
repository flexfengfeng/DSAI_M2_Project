{{ config(materialized='table') }}

with customer_order_stats as (
    select
        customer_id,
        count(*) as total_orders,
        sum(total_order_value) as total_spent,
        avg(total_order_value) as avg_order_value,
        max(total_order_value) as max_order_value,
        min(order_purchase_timestamp) as first_order_date,
        max(order_purchase_timestamp) as last_order_date,
        avg(delivery_days) as avg_delivery_days,
        sum(case when order_status = 'delivered' then 1 else 0 end) as delivered_orders,
        sum(case when delivery_vs_estimate_days <= 0 then 1 else 0 end) as on_time_deliveries
    from {{ ref('int_order_details') }}
    where order_status != 'canceled'
    group by customer_id
)

select
    *,
    case 
        when total_orders = 1 then 'One-time'
        when total_orders between 2 and 3 then 'Repeat'
        when total_orders >= 4 then 'Loyal'
    end as customer_segment,
    
    case
        when total_spent >= 1000 then 'High Value'
        when total_spent >= 300 then 'Medium Value'
        else 'Low Value'
    end as value_segment,
    
    date_diff(last_order_date, first_order_date, day) as customer_lifespan_days,
    delivered_orders / total_orders as delivery_success_rate,
    case 
        when delivered_orders > 0 then on_time_deliveries / delivered_orders 
        else null 
    end as on_time_delivery_rate

from customer_order_stats