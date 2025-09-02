select
DISTINCT supplier_id,
supplier_lead_time
from {{ ref("Consolidated_Table") }}
