{{ config(materialized='table') }}

select
    p.product_id,
    p.product_category_name,
    t.product_category_name_english,
    p.product_name_lenght,
    p.product_description_lenght,
    p.product_photos_qty,
    p.product_weight_g,
    p.product_length_cm,
    p.product_height_cm,
    p.product_width_cm,
    
    -- Calculated fields
    p.product_length_cm * p.product_height_cm * p.product_width_cm as product_volume_cm3,
    
    case 
        when p.product_weight_g < 500 then 'Light'
        when p.product_weight_g < 2000 then 'Medium'
        else 'Heavy'
    end as weight_category,
    
    case 
        when p.product_photos_qty = 0 then 'No Photos'
        when p.product_photos_qty <= 3 then 'Few Photos'
        when p.product_photos_qty <= 6 then 'Good Photos'
        else 'Many Photos'
    end as photo_category

from {{ ref('stg_products') }} p
left join {{ ref('stg_translations') }} t 
    on p.product_category_name = t.product_category_name