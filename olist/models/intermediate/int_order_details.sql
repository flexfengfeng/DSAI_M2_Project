{{ config(materialized='table') }}

with order_items_agg as (
    select
        order_id,
        count(*) as total_items,
        sum(price) as total_product_value,
        sum(freight_value) as total_freight_value,
        sum(price + freight_value) as total_order_value,
        avg(price) as avg_item_price,
        max(price) as max_item_price,
        min(price) as min_item_price
    from {{ ref('stg_order_items') }}
    group by order_id
),

order_payments_agg as (
    select
        order_id,
        sum(payment_value) as total_payment_value,
        count(distinct payment_type) as payment_methods_used,
        max(payment_installments) as max_installments,
        string_agg(distinct payment_type, ', ') as payment_types
    from {{ ref('stg_order_payments') }}
    group by order_id
)

select
    o.order_id,
    o.customer_id,
    o.order_status,
    o.order_purchase_timestamp,
    o.order_approved_at,
    o.order_delivered_carrier_date,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,
    
    -- Order metrics
    oi.total_items,
    oi.total_product_value,
    oi.total_freight_value,
    oi.total_order_value,
    oi.avg_item_price,
    oi.max_item_price,
    oi.min_item_price,
    
    -- Payment metrics
    op.total_payment_value,
    op.payment_methods_used,
    op.max_installments,
    op.payment_types,
    
    -- Delivery metrics
    case 
        when o.order_delivered_customer_date is not null and o.order_purchase_timestamp is not null
        then datetime_diff(o.order_delivered_customer_date, o.order_purchase_timestamp, day)
    end as delivery_days,
    
    case 
        when o.order_delivered_customer_date is not null and o.order_estimated_delivery_date is not null
        then datetime_diff(o.order_delivered_customer_date, o.order_estimated_delivery_date, day)
    end as delivery_vs_estimate_days,
    
    case 
        when o.order_approved_at is not null and o.order_purchase_timestamp is not null
        then datetime_diff(o.order_approved_at, o.order_purchase_timestamp, hour)
    end as approval_time_hours

from {{ ref('stg_orders') }} o
left join order_items_agg oi on o.order_id = oi.order_id
left join order_payments_agg op on o.order_id = op.order_id