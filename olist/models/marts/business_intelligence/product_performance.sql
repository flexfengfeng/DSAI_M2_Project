{{ config(materialized='table') }}

with product_metrics as (
    select
        p.product_id,
        p.product_category_name_english,
        p.weight_category,
        p.photo_category,
        
        count(*) as total_sales,
        sum(f.item_total) as total_revenue,
        avg(f.item_price) as avg_price,
        sum(f.successful_delivery) as successful_deliveries,
        avg(f.delivery_days) as avg_delivery_days,
        
        count(distinct f.customer_id) as unique_customers,
        count(distinct f.seller_id) as unique_sellers

    from {{ ref('fct_orders') }} f
    join {{ ref('dim_products') }} p on f.product_id = p.product_id
    group by 1,2,3,4
)

select
    *,
    successful_deliveries / total_sales as delivery_success_rate,
    total_revenue / total_sales as revenue_per_sale,
    total_sales / unique_customers as sales_per_customer,
    
    -- Ranking within category
    row_number() over(partition by product_category_name_english order by total_revenue desc) as revenue_rank_in_category,
    row_number() over(partition by product_category_name_english order by total_sales desc) as sales_rank_in_category

from product_metrics