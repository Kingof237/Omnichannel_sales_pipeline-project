select
DISTINCT store_id,
store_location,
inventory_level,
reorder_point ,
reorder_quantity
from {{ ref("Consolidated_Table") }}

