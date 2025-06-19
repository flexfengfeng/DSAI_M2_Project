{{
  config(
    materialized='table',
    cluster_by = ['state', 'city']
  )
}}

WITH delivery_time AS (
  SELECT 
    o.order_id,
    o.customer_id,
    -- 将小时转换为天，并保留两位小数
    ROUND(o.delivery_hours / 24.0, 2) AS delivery_days
  FROM {{ ref('stg_orders_delivery') }} o
  WHERE o.delivery_hours IS NOT NULL
),

customers AS (
  SELECT
    customer_id,
    zip_code_prefix
  FROM `brazil-olist.Olist.customer`
  WHERE zip_code_prefix IS NOT NULL
),

avg_delivery_time AS (
  SELECT
    c.zip_code_prefix,
    AVG(d.delivery_days) AS avg_delivery_days,  -- 平均送货天数
    COUNT(d.order_id) AS order_count
  FROM delivery_time d
  JOIN customers c ON d.customer_id = c.customer_id
  GROUP BY 1
  HAVING COUNT(d.order_id) >= 5
)

SELECT
  geo.zip_code_prefix,
  geo.avg_latitude,
  geo.avg_longitude,
  geo.city,
  geo.state,
  a.avg_delivery_days,
  a.order_count,
  -- 添加送货时间分类（基于新的区间划分）
  CASE
    WHEN a.avg_delivery_days <= 7 THEN '0-7天'
    WHEN a.avg_delivery_days <= 14 THEN '8-14天'
    WHEN a.avg_delivery_days <= 21 THEN '15-21天'
    ELSE '22天以上'
  END AS delivery_category
FROM avg_delivery_time a
JOIN {{ ref('stg_geolocation_map') }} geo 
  ON a.zip_code_prefix = geo.zip_code_prefix
WHERE geo.avg_latitude IS NOT NULL
  AND geo.avg_longitude IS NOT NULL
  AND a.avg_delivery_days BETWEEN 0 AND 100