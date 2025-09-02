
-- Fact table combining data from Spotify and Walmart sources
    SELECT 
        transaction_sk,
        transaction_id,
        transtype,
        customer_id,
        supplier_id::TEXT AS supplier_id,
        quantity_sold,
        transaction_date,
        product_id :: TEXT AS product_id,
        unit_price,
        store_id,
        payment_method,
        promotion_applied,
        promotion_type
    FROM {{ ref('Consolidated_Table') }}

   