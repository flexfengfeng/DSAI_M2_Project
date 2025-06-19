{{ config(
    materialized='incremental',
    unique_key='order_item_key'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['oi.order_id', 'oi.order_item_id']) }} as order_item_key,
    oi.order_id,
    oi.order_item_id,
    oi.product_id,
    oi.seller_id,
    od.customer_id,
    sc.state as customer_state,
    
    -- Dates
    od.order_purchase_timestamp,
    extract(year from od.order_purchase_timestamp) as order_year,
    extract(month from od.order_purchase_timestamp) as order_month,
    extract(day from od.order_purchase_timestamp) as order_day,
    extract(dayofweek from od.order_purchase_timestamp) as order_day_of_week,
    
    -- Financial metrics
    oi.price as item_price,
    oi.freight_value as item_freight,
    oi.price + oi.freight_value as item_total,
    od.total_order_value,
    
    -- Order characteristics
    od.order_status,
    od.total_items,
    od.payment_types,
    od.max_installments,
    
    -- Performance metrics
    od.delivery_days,
    od.delivery_vs_estimate_days,
    od.approval_time_hours,
    
    case when od.delivery_vs_estimate_days <= 0 then 1 else 0 end as on_time_delivery,
    case when od.order_status = 'delivered' then 1 else 0 end as successful_delivery

from {{ ref('stg_order_items') }} oi
join {{ ref('int_order_details') }} od on oi.order_id = od.order_id
left join {{ ref('stg_customers') }} sc on od.customer_id = sc.customer_id



{% if is_incremental() %}
where od.order_purchase_timestamp > (select max(order_purchase_timestamp) from {{ this }})
{% endif %}