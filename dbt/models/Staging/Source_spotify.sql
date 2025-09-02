{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

with source_data as (
    select
        order_id,
        product_sku,
        category,
        quantity_sold,
        unit_price,
        transaction_date,
        payment_method,
        sales_amount
    from {{ source('Walmart_data', 'spotify_data') }}
)

select *
from source_data

{% if is_incremental() %}
  where not exists (
      select 1
      from {{ this }} as t
      where t.order_id = source_data.order_id
  )
{% endif %}
