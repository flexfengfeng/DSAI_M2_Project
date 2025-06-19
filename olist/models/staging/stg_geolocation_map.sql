{{
  config(
    materialized='view'
  )
}}

SELECT
  zip_code_prefix,
  AVG(geo_lat) AS avg_latitude,
  AVG(geo_lng) AS avg_longitude,
  ANY_VALUE(city) AS city,  -- 取任一城市名
  ANY_VALUE(state) AS state  -- 取任一州名
FROM `brazil-olist.Olist.geolocation`
GROUP BY 1