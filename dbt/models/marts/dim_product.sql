select
   DISTINCT product_sk,
   product_id,
    product_name,
    category,
    inventory_level ,
    reorder_point,
    reorder_quantity,
    stockout_indicator,
    forecasted_demand,
    actual_demand
from {{ ref("Consolidated_Table") }}

uni
    