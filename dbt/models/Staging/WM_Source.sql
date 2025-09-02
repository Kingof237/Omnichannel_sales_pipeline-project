{{ config(
    materialized='incremental',
    unique_key='transaction_id'
) }}

with source_data as (
    select
        transaction_id,
        customer_id,
        product_id,
        product_name,
        category,
        quantity_sold,
        unit_price,
        transaction_date,
        store_id,
        store_location,
        inventory_level,
        reorder_point,
        reorder_quantity,
        supplier_id,
        supplier_lead_time,
        customer_age,
        customer_gender,
        customer_income,
        customer_loyalty_level,
        payment_method,
        promotion_applied,
        promotion_type,
        weather_conditions,
        holiday_indicator,
        weekday,
        stockout_indicator,
        forecasted_demand,
        actual_demand
    from {{ source('Walmart_data', 'walmart_sales') }}
)

select *
from source_data

{% if is_incremental() %}
  where not exists (
      select 1
      from {{ this }} as t
      where t.transaction_id = source_data.transaction_id
  )
{% endif %}
